from ..texts import ButtonTexts

class InlineKeyboards:
    def __init__(self, lang: str = 'ru'):
        self.texts = ButtonTexts(lang)

__all__ = ["InlineKeyboards"]