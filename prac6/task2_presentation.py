side1 = float(input('Сторона 1: '))
side2 = float(input('Сторона 2: '))
side3 = float(input('Сторона 3: '))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print('Треугольник равносторонний')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')