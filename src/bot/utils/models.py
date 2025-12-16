from src.common.constants import DEFAULT_LANGUAGE


class BaseTextHolder:
    """Базовый класс для текстов"""

    def __init__(self, lang: str = DEFAULT_LANGUAGE):
        self._lang: str = lang

        for key, value in self.__class__.__dict__.items():
            if isinstance(value, dict):
                setattr(self, key, value.get(lang) or value.get(DEFAULT_LANGUAGE, ''))


class TextHolder(BaseTextHolder):
    """Тексты обычных сообщений"""
    pass


class ButtonTextHolder(BaseTextHolder):
    """Тексты кнопок"""
    pass
