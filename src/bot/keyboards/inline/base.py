from aiogram.types import InlineKeyboardMarkup


class BaseInlineKeyboard:
    """Базовый класс для inline-клавиатур с поддержкой локализации."""

    def __init__(self, texts):
        self.texts = texts