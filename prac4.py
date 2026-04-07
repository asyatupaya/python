import math


BASH_BOLD = '\033[1m'
BASH_DEFAULT = '\033[0m'


def calc_distance(point1: tuple[int | float, int | float], point2: tuple[int | float, int | float]) -> float:
    """
    Вычисление расстояния между двумя точками

    :param point1: Кортеж координат первой точки в у.е.
    :param point2: Кортеж координат второй точки в у.е.
    :return: None
    """

    distance: float = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance

def main(*args, **kwargs) -> None:

    # Ввод координат
    (x1, y1) = map(float, input('Введите координаты ПЕРВОЙ точки в формате x;y\nКоординаты: ').split(';'))
    (x2, y2) = map(float, input('Введите координаты ВТОРОЙ точки в формате x;y\nКоординаты: ').split(';'))

    # Получение дистанции
    distance = calc_distance((x1, y1), (x2, y2))
    print(f'{BASH_BOLD}Расстояние между точками: {distance:.2f} у.е.{BASH_DEFAULT}')


main()