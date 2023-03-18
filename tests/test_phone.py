from src.phone import Phone
import pytest

@pytest.fixture()
def test_object():
    return Phone("Nokia", 10000, 20)

def test_item_number_of_sim(test_object):
    assert (test_object.number_of_sim) == 1

