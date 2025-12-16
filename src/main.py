from contextlib import asynccontextmanager
import asyncio
import sys
from loguru import logger

from src.common import db
from app.bot import start_bot


logger.remove()  # убираем стандартный sink
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>"
)


async def main():
    await db.init()
    try:
        await start_bot()
    finally:
        await db.dispose()


if __name__ == "__main__":
    asyncio.run(main())