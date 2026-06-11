print('Проверка чётности всех чисел')
print('Введите последовательность из 10 чисел')

isUneven = False

for i in range(1, 11):
    num = int(input(f'{i}: '))
    if num % 2 != 0:
        isUneven = True

print(f'{'YES (все четные)' if not isUneven else 'NO (есть нечётные)'}')
