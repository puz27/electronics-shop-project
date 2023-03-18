from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = 1):
        super().__init__(name, price, quantity)
        if self.validate_sim_count(number_of_sim):
            self.__number_of_sim = number_of_sim
        else:
            raise Exception("Недопустимое количество карт")

    def __repr__(self):
        return f"Phone{self.name, self.price, self.quantity, self.number_of_sim}"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        self.__number_of_sim = new_number_of_sim

    @classmethod
    def validate_sim_count(cls, number_of_sim):
        return number_of_sim < 4

# x = Phone("TV1fdgfdgdfgdfgfd111", 10, 10, 3)
# x.pay_rate = 0.5
# x.apply_discount()
# print(x.calculate_total_price())
#print(x.__dict__)

