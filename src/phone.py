from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = 1) -> None:
        """
        Создание экземпляра класса Phone. Наследуется от класса Item
        :param number_of_sim: количество сим карт
        """
        super().__init__(name, price, quantity)
        if self.validate_sim_count(number_of_sim):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        """Дандер для вывода информации об экземпляре"""
        return f"Phone{self.name, self.price, self.quantity, self.number_of_sim}"

    @property
    def number_of_sim(self):
        """Устанавливает количество карт телефону """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        """Получает количество карт телефона """
        if self.validate_sim_count(new_number_of_sim):
            self.__number_of_sim = new_number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    @classmethod
    def validate_sim_count(cls, number_of_sim):
        """Проверка корректности ввода информации для сим карт"""
        return (0 < number_of_sim < 4) and type(number_of_sim) is int

    def __add__(self, other):
        """Дандер для реализации сложения количесва товаров класса"""
        if isinstance(other, Phone) or isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError("Нельзя складывать с экземплярами классов не принадлежащих Phone или Item")
