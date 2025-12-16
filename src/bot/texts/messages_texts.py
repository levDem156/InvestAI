from ..utils import TextHolder


class MenuTexts(TextHolder):
    '''Тексты меню'''

    START_TEXT = {
        'ru': '\n'.join([
            "Привет! Я InvestAI — твой личный помощник в мире инвестиций. 🤖📈"
        ]),

        'en': '\n'.join([
            "Hello! I'm InvestAI, your personal assistant in the world of investments. 🤖📈",
        ])
    }


class Texts:
    '''Все тексты'''

    def __init__(self, lang):
        self.menu = MenuTexts(lang)
