import csv
from src.csverror import InstantiateCSVError


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
            raise ValueError("Длина наименования товара превышает 10 символов.")

    @property
    def name(self) -> str:
        """Возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Присваивает название товару"""
        if self.validate_name(new_name):
            self.__name = new_name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")


    def calculate_total_price(self) -> float:
        """
        Расчитывает общую стоимость конкретного товара в магазине
        :return: Общая стоимость товара
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара"""
        self.price = self.price * self.pay_rate

    @classmethod
    def validate_name(cls, name: str) -> int:
        """Проверка названия на длину"""
        return len(name) <= 10

    @classmethod
    def instantiate_from_csv(cls, path: str ="../src/items.csv") -> None:
        """Cоздаем экзепляры класса на основе данных их файла"""
        all_info = []

        try:
            with open(path, encoding="CP1251") as csv_file:
                take_csv_data = csv.reader(csv_file, delimiter=",")
                count = 0
                for roe in take_csv_data:
                    if count != 0:
                        all_info.append(roe)
                    else:
                        if len(roe) != 3:
                            raise InstantiateCSVError

                        count += 1
        except InstantiateCSVError:
            csv_error = InstantiateCSVError()
            print(csv_error)
        except Exception:
            print("Отсутствует файл item.csv")

        for data in all_info:
            cls(*data)

    @staticmethod
    def string_to_number(number: str) -> int:
        """Cтатический метод, возвращающий число из числа-строки
        :return: Число в нужном нам формате
        """
        return int(number.split(".")[0])

    def __str__(self) -> str:
        """Дандер для вывода информации об экземпляре"""
        return f"{self.__name}"

    def __repr__(self) -> str:
        """Дандер для вывода информации об экземпляре"""
        return f"Item{self.__name, self.price, self.quantity}"

    def __add__(self, other: any) -> int or ValueError:
        """Дандер для реализации сложения количесва товаров класса"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError("Нельзя складывать с экземплярами классов не принадлежащих классу Item")
