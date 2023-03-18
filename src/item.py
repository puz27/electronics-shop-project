import os
from src.utils import load_csv


class Item:
    """Класс для представления товара в магазине"""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item
        :param name: Название товара
        :param price: Цена за единицу товара
        :param quantity: Количество товара в магазине
        """
        if self.validate_name(name):
            self.__name = name
            self.price = price
            self.quantity = quantity
            self.all.append(self)
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @property
    def name(self) -> str:
      return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине
        :return: Общая стоимость товара
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара"""
        self.price = self.price * self.pay_rate

    @classmethod
    def validate_name(cls, name):
        return len(name) <= 10

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Cоздаем экзепляры класса на основе данных их файла"""
        cls.all = []
        for data in load_csv():
            cls(*data)

    @staticmethod
    def string_to_number(number: str) -> int:
        """Cтатический метод, возвращающий число из числа-строки
        :return: Число в нужном нам формате
        """
        return int(number.split(".")[0])

    def __str__(self):
        """Тандер для вывода информации об экземпляре"""
        return f"{self.__name}"

    def __repr__(self):
        """Тандер для вывода информации об экземпляре"""
        return f"Item{self.__name, self.price, self.quantity}"

    def __add__(self, other):
        self.quantity + other.quantity
