from typing import List

"""
Поиск второго максимального элемента в массиве
"""

def find_second_max_element(numbers: List[int]) -> int | None:
    for num1 in numbers:
        if not isinstance(num1, int):
            raise ValueError("элементы массива  некорректного типа данных")

    if len(numbers) < 2:
        return None

    max1 = numbers[0]
    max2 = None

    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or (num > max2 and num != max1):
            max2 = num


    return max1

