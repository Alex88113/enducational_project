from typing import List, Any, Callable
from pathlib import Path

from loguru import logger

file = Path(__file__)
logger.info("Импорт декораторов в модуль: {module}", module=file)

try:
    from decorate_for_check_type import (
        check_type_numbers_list,
        check_type_strings_list)

    logger.info("импорт декораторов из decorate_for_check_type в {m} произведен успешно!",  m=file)

except ModuleNotFoundError as error:
    logger.error("возникла ошибка при импорте модуля: {e}", e=error)

except ImportError as error:
    logger.error("Ошибка при перемещении модуля: {e}", e=error)


@check_type_numbers_list
def check_sorted_list(numbers: List[int]) -> bool:
    if len(numbers) < 2:
        return True # пустой список считается отсортированным

    for i in range(0, len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True


@check_type_strings_list
def delete_duplicate_elements(letters_list: List[str]) -> List[str]:
    result = []
    seen = set()

    for element in letters_list:
        if element not in seen:
            result.append(element)
            seen.add(element)

    return result

"""
Слияние двух массивов
"""

@check_type_numbers_list
def merge_two_list(numbers: List[int], numbers2: List[int]) -> List[int]:
    result = []
    i = 0 # second element
    j = 0 # first element

    while i < len(numbers) and j < len(numbers2):
        if numbers[i] <= numbers2[j]:
            result.append(numbers[i])
            i += 1

        else:
            result.append(numbers2[j])
            j += 1

    result.extend(numbers[i: ])
    result.extend(numbers2[j: ])

    return result


