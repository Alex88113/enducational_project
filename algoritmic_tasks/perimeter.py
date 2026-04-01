def calculate_perimeter(length: int, width: float) -> float:
    if not isinstance(length, int) or length < 0:
        raise ValueError("длина не является целым числом либо оно отрицательно")

    if not isinstance(width, float) or width < 0:
        raise ValueError("ширина не вещественное число либо она отрицательна")

    return 2 * (length + width)

print(calculate_perimeter(10, 90.4))