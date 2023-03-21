from src.item import Item


class KeyboardMixin:
   
    def change_lang(self, set_language):
        self.__language = set_language


class KeyBoard(Item):

    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.language

    @language.setter
    def language(self, new_language):
        self.__language = new_language

    @classmethod
    def validate_name(cls, name):
        """Проверка названия на длину для клавиатуры"""
        return len(name) <= 20
