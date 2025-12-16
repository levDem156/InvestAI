from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger, Numeric
from sqlalchemy.orm import Mapped
from datetime import datetime

from ..core import Base
from .enums import TransactionType


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_telegram_id = Column(BigInteger, nullable=False, index=True)                   # Связь с пользователем по telegram_id
    type: Mapped[TransactionType] = Column(String(20), nullable=False, index=True)      # Тип операции
    symbol = Column(String(20), nullable=True, index=True)                              # Тикер/актив
    quantity = Column(Numeric(20, 8), default=0, nullable=False)                        # Количество актива
    price = Column(Numeric(20, 8), nullable=True)                                       # Цена за единицу актива
    amount = Column(Numeric(20, 2), nullable=False)                                     # Влияние на денежный баланс (положительное или отрицательное)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)   # Когда произошла операция
