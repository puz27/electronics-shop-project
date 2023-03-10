from src.item import Item
import pytest


@pytest.fixture
def test_object():
    return Item("Potato", 100.5, 50)


def test_item_calculate_total_price(test_object):
    assert test_object.calculate_total_price() == 5025.0


def test_item_apply_discount(test_object):
    test_object.apply_discount()
    assert test_object.price == 100.5


def test_string_to_number():
    assert Item.string_to_number('567.432') == 567


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert (len(Item.all) - 1) == 4