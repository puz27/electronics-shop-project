from src.item import Item


class KeyboardMixin:

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        """Изменяет раскладку клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self) -> str:
        """Возвращает раскладку клавиатуры"""
        return self.__language

    @language.setter
    def language(self, new_language: str) -> str or ValueError:
        """Устанавливает раскладку клавиатуры"""
        if new_language == "EN" or new_language == "RU":
            self.__language = new_language
        else:
            raise AttributeError("У клавиатуры только два языка: EN/RU")


class KeyBoard(Item, KeyboardMixin):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса KeyBoard. Наследуется от класса Item, KeyboardMixin"""
        Item.__init__(self, name, price, quantity)
        KeyboardMixin.__init__(self)

    @classmethod
    def validate_name(cls, name: str) -> bool:
        """Проверка названия на длину для клавиатуры"""
        return len(name) <= 20
