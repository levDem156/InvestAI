from typing import Optional
from sqlalchemy.future import select

from ..models import Transaction


class TransactionRepository:
    def __init__(self, db):
        self.db = db

    async def create_transaction(self, user_telegram_id: int, **kwargs) -> Transaction:
        """
        Создаёт новую сделку и возвращает объект Transaction.
        """
        kwargs = {k: None if v == "" else v for k, v in kwargs.items()}

        async with self.db.async_session() as session:
            async with session.begin():
                # Создаём новую сделку

                transaction = Transaction(user_telegram_id=user_telegram_id, **kwargs)
                session.add(transaction)

                await session.flush()
                await session.refresh(transaction)
                return transaction
