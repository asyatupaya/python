print('Таблица умножения')
num = int(input('Введите натуральное число от 1 до 10: '))

if 1 <= num <= 10:
    for i in range(1, 11):
        print(f'{num} * {i} = {num * i}')
else:
    print('Ну нормально же попросил')
