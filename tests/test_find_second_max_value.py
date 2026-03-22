import pytest

from loguru import logger

logger.info("Импорт модуля medium_task...")

try:
    from meduim_tasks import find_second_max_element
    logger.info("Импорт произведен успешно")

except ModuleNotFoundError as error_import:
    logger.error("Ошибка при импорте модулей: {e}", e=error_import)

except ImportError as error_import:
    logger.error("проблемы при перемещении модуля: {e}", e=error_import)

class TestFindSecondMax:
    @pytest.mark.parametrize("list_numbers, expected_result", [
        ([10, 34, 54, 65, 34], 65),
        ([100, 4554, 344, 89, -1], 4554),
        ([955, 93, 56, 845], 955)
    ])

    def test_find_second_max_value(self, list_numbers, expected_result):
        assert find_second_max_element(list_numbers) == expected_result

    @pytest.mark.parametrize("list_numbers, expected_result", [
        ([], None),
        ([100, 4554, 344, 89, -1], 4554),
        ([955, 93, 56, 845], 955)
    ])

    def test_find_second_max_value2(self, list_numbers, expected_result):
        assert find_second_max_element(list_numbers) == expected_result

