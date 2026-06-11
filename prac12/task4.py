marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

fives = 0
twos = 0

for elem in marks:
    if elem == 5: fives += 1
    elif elem == 2: twos += 1

print(f'Пятёрки: {fives}')
print(f'Двойки: {twos}')
