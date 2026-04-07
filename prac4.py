import math


(x1, y1) = map(float, input('Введите ккординаты ПЕРВОЙ точки в формате x;y\nКоординаты: ').split(';'))
(x2, y2) = map(float, input('Введите ккординаты ВТОРОЙ точки в формате x;y\nКоординаты: ').split(';'))

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f'Расстояние между точками: { distance:.2f } ед.')