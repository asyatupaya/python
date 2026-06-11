print('Наибольшие числа')
iterations = int(input('Введите натуральное число ≥ 2: '))

max1 = None
max2 = None

if iterations >= 2:
    print(f'Введите {iterations} натуральных')
    for i in range(iterations):
        num = int(input(f'{i + 1}: '))
        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or num > max2:
            max2 = num
    print(f'Первое максимальное: {max1}')
    print(f'Второе максимальное: {max2}')
else:
    print('Ну нормально же попросил')