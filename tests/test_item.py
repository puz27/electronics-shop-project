from src.item import Item
import pytest
from src.csverror import InstantiateCSVError


@pytest.fixture
def test_object():
    return Item("Potato", 100.5, 50)


def test_item_calculate_total_price(test_object):
    """Проверка общей стоимости товаров"""
    assert test_object.calculate_total_price() == 5025.0


def test_item_apply_discount(test_object):
    """Проверка применения дискона. По умолчанию значение 1"""
    test_object.apply_discount()
    assert test_object.price == 100.5


def test_string_to_number():
    """Проверка вывода числа как целого числа"""
    assert Item.string_to_number('567.432') == 567


def test_str_item(test_object):
    """Проверка вывода информации о тоываре"""
    assert (str(test_object)) == "Potato"


def test_repr_item(test_object):
    """Проверка вывода информации о товаре"""
    assert (repr(test_object)) == "Item('Potato', 100.5, 50)"


def test_item_name(test_object):
    """Проверка на длину наименования"""
    with pytest.raises(ValueError, match="Длина наименования товара превышает 10 символов."):
        test_object.name = "Тестовое название телефона"


def test_item_add(test_object):
    """Проверка сложения экземпляроа класса по количеству"""
    test_1 = Item("Potato", 100.5, 50)
    test_2 = Item("Melon", 100.5, 50)
    assert (test_1 + test_2) == 100


def test_load_csv_1():
    """Проверка корректной загрузки"""
    assert Item.instantiate_from_csv("../tests/test_items.csv") == None


def test_load_csv_2(capsys):
    """Проверка существования файла"""
    Item.instantiate_from_csv(path="../tests/test_items1.csv")
    captured = capsys.readouterr()
    assert captured.out == 'Отсутствует файл item.csv\n'


def test_load_csv_3(capsys):
    """Проверка корректности файла"""
    Item.instantiate_from_csv(path="../tests/test_items2.csv")
    captured = capsys.readouterr()
    assert captured.out == 'Файл item.csv поврежден\n'
