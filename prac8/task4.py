print('Вычисление популяции')
start = int(input('Стартовое количество: '))
multiplier = int(input('Процент увеличения в день: ')) / 100
days = int(input('Количество дней для размножения: '))

population = start
print(f'Начальное количество: {population}')

for i in range(days):
    population += population * multiplier
    print(f'День {i + 1}: {round(population, 2)}')
