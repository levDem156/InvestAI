from enum import StrEnum, auto

class TransactionType(StrEnum):
    DEPOSIT = auto()   # "deposit"  — пополнение счёта
    WITHDRAW = auto()  # "withdraw" — вывод средств
    BUY = auto()       # "buy"      — покупка актива
    SELL = auto()      # "sell"     — продажа актива