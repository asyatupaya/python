from math import pi


def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Вычислить площадь прямоугольника в у.е.

    :param width: float
    :param height: float
    :return: float
    """

    area = width * height
    return area


def  calculate_circle_area(radius: float) -> float:
    """
    Вычислить площадь круга в у.е.

    :param radius: float
    :return: float
    """

    area = pi * (radius ** 2)
    return area


(rect_width, rect_height) = map(float, input('Введите стороны прямоугольника через пробел: ').split())
circle_radius = input('Введите стороны прямоугольника через пробел: ')

### ДОДЕЛАТЬ
