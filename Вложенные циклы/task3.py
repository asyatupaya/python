from math import isqrt


num1 = int(input('Введите натуральное число: '))
num2 = int(input(f'Введите натуральное число БОЛЬШЕ {num1}: '))

if num2 > num1:
    for num in range(num1, num2 + 1):
        # проверка базовых условий
        if num <= 1: continue
        if num % 2 == 0 and num != 2: continue

        # пройтись по всем числам от 3 до корня из числа включительно
        is_simple = True
        for i in range(3, int(isqrt(num)) + 1, 2):
            # проверяем, делится ли число без остатка
            if num % i == 0: is_simple = False
            break

        if is_simple: print(f'Простое: {num}')
else:
    print('НЕТ!!! НЕПРАВИЛЬНЫЕ ЧИСЛА')