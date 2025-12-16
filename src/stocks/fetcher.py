from decimal import Decimal
from typing import Optional

from tinkoff.invest.schemas import Quotation

from .client import TinkoffClient
from .cache import get_price, set_price


def _quotation_to_decimal(quotation: Quotation) -> Decimal:
    """Конвертирует Quotation (units + nano) в Decimal"""
    return Decimal(f"{quotation.units}.{abs(quotation.nano):09d}".rstrip("0").rstrip("."))


async def get_price(symbol: str) -> Optional[Decimal]:
    """
    Получает текущую цену по тикеру (например, 'SBER', 'AAPL', 'USD000UTSTOM').
    Сначала проверяет кэш, потом запрашивает API.
    """
    symbol = symbol.upper()

    # 1. Проверяем кэш
    cached = get_price(symbol)
    if cached is not None:
        return cached

    # 2. Запрос в Tinkoff API
    try:
        with TinkoffClient.get_client() as client:
            # Находим инструмент по тикеру
            response = client.instruments.find_instrument(query=symbol)
            instruments = response.instruments
            if not instruments:
                return None

            figi = instruments[0].figi

            # Получаем последнюю цену
            last_prices = client.market_data.get_last_prices(figi=[figi])
            if not last_prices.last_prices:
                return None

            price_quotation = last_prices.last_prices[0].price
            price = _quotation_to_decimal(price_quotation)

            # Сохраняем в кэш
            set_price(symbol, price)
            return price

    except Exception as e:
        # В продакшене лучше логировать
        print(f"Ошибка получения цены {symbol}: {e}")
        return None