from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger, Numeric
from datetime import datetime

from ..core import Base
from src.common.constants import DEFAULT_LANGUAGE


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False, index=True)           # Уникальный Telegram ID
    username = Column(String, nullable=True)                                            # Username Telegram
    first_name = Column(String(255), nullable=False)                                    # Имя пользователя
    last_name = Column(String(255), nullable=True)                                      # Фамилия пользователя
    language_code = Column(String(10), default=DEFAULT_LANGUAGE, nullable=False)        # Язык пользователя
    balance = Column(Numeric(20, 2), default=0.00, nullable=False)                      # Баланс пользователя
    is_active = Column(Boolean, default=True)                                           # Активен ли пользователь
    created_at = Column(DateTime, default=datetime.utcnow)                              # Дата создания записи
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)    # Дата обновления записи
