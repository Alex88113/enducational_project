import pytest

from perimeter import calculate_perimeter

@pytest.mark.parametrize("length, width, expected_result", [
    (10, 90.4, 200.8),
    (100, 200.4, 600.8),
    (9, 20.6, 59.2)
])

def test_perimeter(length, width, expected_result):
    assert calculate_perimeter(length, width) == expected_result

@pytest.mark.parametrize("bag_value1, bag_value2", [
    (-1, -1),
    ('fefef', '3434dfleld'),
    (True, None)
])

def test_exception_perimeter(bag_value1, bag_value2):
    with pytest.raises(ValueError):
       assert calculate_perimeter(bag_value1, bag_value1)