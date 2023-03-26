from src.keyboard import KeyboardMixin, KeyBoard
import pytest


@pytest.fixture
def test_object():
    return KeyBoard("Logitech", 50, 10)


def test_keyboard(test_object):
    """Проверка вывода информации о клавиатуре"""
    assert(str(test_object)) == "Logitech"


def test_keyboard_language_1(test_object):
    """Проверка языка по умолчанию для клавиатуры"""
    assert (str(test_object.language)) == "EN"


def test_keyboard_language_2(test_object):
    """Проверка смены языка для клавиатуры"""
    test_object.change_lang()
    assert (str(test_object.language)) == "RU"


def test_keyboard_len_name():
    """Проверка длины названия для класса KeyBoard"""
    with pytest.raises(ValueError, match="Длина наименования товара превышает 10 символов."):
        KeyBoard("Dell Long Descripton for test", 5, 5)
