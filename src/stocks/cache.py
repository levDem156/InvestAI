from datetime import datetime, timedelta
from typing import Optional
from decimal import Decimal

# Кэш: {symbol: {'price': Decimal, 'updated_at': datetime}}
_price_cache: dict[str, dict] = {}
CACHE_TTL = timedelta(minutes=1)  # Цена актуальна 1 минуту


def set_price(symbol: str, price: Decimal):
    _price_cache[symbol.upper()] = {
        "price": price,
        "updated_at": datetime.utcnow()
    }


def get_price(symbol: str) -> Optional[Decimal]:
    symbol = symbol.upper()
    data = _price_cache.get(symbol)
    if data and datetime.utcnow() - data["updated_at"] < CACHE_TTL:
        return data["price"]
    return None


def invalidate_price(symbol: str):
    _price_cache.pop(symbol.upper(), None)