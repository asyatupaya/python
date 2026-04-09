color1 = input('Введите первый основной цвет: ').lower()
color2 = input('Введите второй основной цвет: ').lower()

if not (color1 == 'красный' or color1 == 'синий' or color1 == 'желтый'):
    print('Первый основной цвет не существует')
elif not (color2 == 'красный' or color2 == 'синий' or color2 == 'желтый'):
    print('Второй основной цвет не существует')
else:
    if (color1 == 'красный' and color2 == 'синий') or (color1 == 'синий' and color2 == 'красный'):
        print('При смешивании: Фиолетовый')
    elif (color1 == 'красный' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'красный'):
        print('При смешивании: Оранжевый')
    elif (color1 == 'синий' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'синий'):
        print('При смешивании: Зеленый')
    else:
        print(f'При смешивании: {color1}')