word = input('Введите слово: ')

list = list(word)
reverse_list = list[::-1]

if list == reverse_list:
    print('Палиндром')
else:
    print('Не палиндром')
