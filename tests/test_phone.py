from src.phone import Phone
import pytest


@pytest.fixture()
def test_object():
    return Phone("Nokia", 10000, 20)


def test_item_number_of_sim(test_object):
    """Проверка на количество сим карт по умолчанию"""
    assert (test_object.number_of_sim) == 1


def test_item_number_of_sim_2(test_object):
    """Проверка на количество сим карт """
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        test_object.number_of_sim = 10


def test_item_number_of_sim_3(test_object):
    """Проверка на количество сим карт при инициализации экземплдяра"""
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        Phone("Nokia", 10000, 20, 10)


def test_item_name(test_object):
    """Проверка на длину наименования"""
    with pytest.raises(ValueError, match="Длина наименования товара превышает 10 символов."):
        test_object.name = "Тестовое название телефона"


def test_item_repr(test_object):
    """Проверка вывода информации о телефоне"""
    assert (repr(test_object)) == "Phone('Nokia', 10000, 20, 1)"


def test_item_get_sim_counts(test_object):
    """Проверка на изменение количества поддерживаемых сим карт"""
    test_object.number_of_sim = 3
    assert (test_object.number_of_sim) == 3


def test_item_add(test_object):
    """Проверка сложения экземпляроа класса по количеству"""
    test_1 = Phone("Nokia", 100, 50)
    test_2 = Phone("Sony", 100, 50)
    assert (test_1 + test_2) == 100
