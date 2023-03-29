from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("../tests/test_items1.csv")
    # FileNotFoundError: Отсутствует файл item.csv
    Item.instantiate_from_csv("../tests/test_items2.csv")
    # InstantiateCSVError: Файл item.csv поврежден

