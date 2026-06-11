weight = float(input('Введите свой вес (кг): '))

if not (0 < weight < 69):
    print('Вы не подходите')
else:
    if weight < 60:
        print('Весовая категория: лёгкий вес')
    elif weight < 64:
        print('Весовая категория: первый полусредний вес')
    elif weight < 69:
        print('Весовая категория: полусредний вес')
