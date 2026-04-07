# consts
TAX = 0.13


income = float(input('Введите ваш доход за год (руб.): '))
income_str = f'{income:_.2f}'.replace('_', ' ')
print(f'\nОбщая сумма дохода: {income_str} руб.')

total_tax = income * TAX
total_tax_str = f'{total_tax:_.2f}'.replace('_', ' ')
print(f'Сумма рассчитанного налога: {total_tax_str} руб.')

total_amount = income - total_tax
total_amount_str = f'{total_amount:_.2f}'.replace('_', ' ')
print(f'Сумма «на руки» после вычета налога: {total_amount_str} руб.')
