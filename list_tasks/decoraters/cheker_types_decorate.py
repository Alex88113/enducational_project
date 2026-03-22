from typing import List, Any, Callable
from functools import wraps

from loguru import logger


def check_type_numbers_list(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs:  Any) -> Any:
        logger.debug("Начало проверки типов параметров числовых массивов")
        parameter: Any = args[0]

        if not isinstance(parameter, list):
            logger.error("переданный объект списком")
            raise ValueError("переданный объект списком")

        for value in parameter:
            if not isinstance(value, int):
                logger.error("в функции {f} элементы списка не являются целыми числами", f=func.__name__)
                raise ValueError(f"в функции {func.__name__} элементы списка не являются целыми числами")

        result = func(*args, **kwargs)
        logger.debug("проверка данных завершена успешно")
        logger.info("Полученный результат: {r}", r=result)
        logger.info("-" * 60)

        logger.info('\n')
        return result

    return wrapper


def check_type_strings_list(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs:  Any) -> Any:
        logger.debug("Начало проверки типов параметров строковых массивов")
        parameter: Any = args[0]

        if not isinstance(parameter, list):
            logger.error("переданный объект списком")
            raise ValueError("переданный объект списком")

        for value in parameter:
            if not isinstance(value, str):
                logger.error("в функции {f} элементы списка не являются ни строковым форматом", f=func.__name__)
                raise ValueError(f"в функции {func.__name__} элементы списка не являются строковым форматом")

        result = func(*args, **kwargs)
        logger.debug("проверка данных завершена успешно")
        logger.info("Полученный результат: {r}", r=result)
        logger.info('-' * 60)
        logger.info('\n')

        return result

    return wrapper

