from src.item import Item
from src.csverror import InstantiateCSVError
import pytest

def test_load_csv_1():
    """Проверка общей стоимости товаров"""
    assert Item.instantiate_from_csv("../tests/test_items.csv") == None
