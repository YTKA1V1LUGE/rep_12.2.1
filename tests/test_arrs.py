from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_slice_length():
    """Проверка если список пуст"""
    assert arrs.my_slice([], 0) == []


def test_slice_start_is_none():
    "Проверка если старт с None"
    assert arrs.my_slice([1, 2, 3], None) == [1, 2, 3]


def test_slice_end_is_none():
    assert arrs.my_slice([1, 2, 3], 0, None) == [1, 2, 3]
