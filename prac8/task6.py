import random as r


ATTEMPTS = 3
MIN_NUM = 1
MAX_NUM = 10

isWin = False

print('Угадай число')
secret = r.randint(MIN_NUM, MAX_NUM)

print(f'Отгадай загаданное число от {MIN_NUM} до {MAX_NUM} за {ATTEMPTS} попыток')
for i in range(ATTEMPTS):
    num = int(input(f'{i + 1}: '))
    if secret == num:
        print('ТЫ ОТГАДАЛ!')
        isWin = True
        break
    elif secret > num:
        print('Загаданное число больше!')
    elif secret < num:
        print('Загаданное число меньше!')
print('Ты выиграл!' if isWin else 'Ты проиграл!')
