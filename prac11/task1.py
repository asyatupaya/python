def equation(n:int, k:int, m:int):
    result = 28 * n + 30 * k + 31 * m
    return True if result == 365 else False

for n in range(12):
    for k in range(12):
        for m in range(12):
            if equation(n, k, m): print(f'{n},{k},{m}')