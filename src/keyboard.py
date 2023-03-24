from src.item import Item


class KeyboardMixin:

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

    def __init__(self, name: str, price: float, quantity: int, language: str = "EN") -> None:
        """Создание экземпляра класса KeyBoard. Наследуется от класса Item, KeyboardMixin"""
        super().__init__(name, price, quantity)
        self.language = language

    @classmethod
    def validate_name(cls, name: str) -> bool:
        """Проверка названия на длину для клавиатуры"""
        return len(name) <= 20
