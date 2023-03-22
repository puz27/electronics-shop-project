from src.item import Item


class KeyboardMixin:

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language):
        if new_language == "EN" or new_language == "RU":
            self.__language = new_language
        else:
            raise AttributeError("У клавиатуры только два языка: EN/RU")


class KeyBoard(Item, KeyboardMixin):

    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language

    @classmethod
    def validate_name(cls, name):
        """Проверка названия на длину для клавиатуры"""
        return len(name) <= 20

