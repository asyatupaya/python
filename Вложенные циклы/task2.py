number = abs(int(input('Введите натуральное число: ')))
str_number = str(number)

while True:
    # summa = sum(int(char) for char in str_number)
    # альтернативный способ найти сумму с for
    summa = sum(map(int, str_number))
    if summa < 10:
        print(f'> Цифровой корень числа {number} = {summa}!')
        break
    print(f'Сумма: {summa}')
    print('Продоложаем складывать')
    str_number = str(summa)
