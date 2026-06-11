print('Знакочередующаяся сумма')
num = int(input('Введите натуральное число (количество итераций): '))

summ = 0
isPlus = True

for i in range(1, num + 1):
    summ += i if isPlus else -i
    isPlus = not isPlus

print(f'Сумма: {summ}')
