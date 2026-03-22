from loguru import logger

logger.debug("Начало импорта...")

try:
    from new_medium_tasks2 import (
        delete_duplicate_elements,
        check_sorted_list,
        merge_two_list
    )

    logger.debug("импорт произведен успешно")

except ModuleNotFoundError as error:
    logger.error("возникла ошибка при импорте модуля: {e}", e=error)

except ImportError as error:
    logger.error("Ошибка при перемещении модуля: {e}", e=error)


def main() -> None:
    sorted_func = None
    delete_elements = None

    try:
        sorted_func = check_sorted_list([12, 5454, 76, 4, 77, 43])
        delete_elements = delete_duplicate_elements(['a', 'b', 'c', 'a', 'b', 'c', 'a'])
        print(merge_two_list([1, 3, 5, 7], [2, 4, 6]))

    except ValueError as error:
        logger.error("Некорректный тип параметров")

    except Exception as error:
        logger.error("Возникла непредвиденная ошибка: {e}", e=error)

    print(f'Результат отсортированной функции: {sorted_func}')
    print(f'Список с удаленными дубликатами: {delete_elements}')

if __name__ == "__main__":
    main()

