from random import randint

numbers = []

for i in range(5):
    numbers.append(randint(0, 100))

print(f'Случайные числа: {numbers}')

min_value = min(numbers)
print(f'Минимальное: {min_value}')

min_index = numbers.index(min_value)

numbers[0], numbers[min_index] = numbers[min_index], numbers[0]
print(f'Поменяли местами: {numbers}')
