# input
(weight, height) = map(float, input('Введите вес (кг) и рост (м) через пробел: ').split())

imt = weight / (height ** 2)
print(f'Ваш ИМТ: {imt:.1f}')

