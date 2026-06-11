prices = [100, 50, 200, 150]

print(f'Минимальная: {min(prices)}')
print(f'Максимальная: {max(prices)}')
print(f'Средняя: {sum(prices)/len(prices)}')
print(*prices, sep=', ')
