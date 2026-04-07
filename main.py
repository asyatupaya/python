"""
Практическая №8
Задание: определить купе по месту посадки
"""

# Количество мест в купе
SEATS_IN_COMPARTMENT = 4

seat_number = int(input('Введите ваш посадочный номер: '))
compartment_number = ((seat_number - 1) // SEATS_IN_COMPARTMENT ) + 1
print(f'Ваше купе: { compartment_number }')
