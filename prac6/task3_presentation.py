month_num = int(input('Введите порядковый номер месяца: '))

if not (1 <= month_num <= 12):
    print('Такого месяца нет')
else:
    if month_num == 2:
        print('В месяце 28 дней')
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        print('В месяце 30 дней')
    else:
        print('В месяце 31 день')