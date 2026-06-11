bik = 10
korova = 5
telenok = 0.5

def equation(b, k, t):
    result = b * bik + k * korova + t * telenok
    return True if result == 100 else False

print('Бык', 'Корова', 'Телёнок')
for b in range(1, int(100 / bik)):
    for k in range(1, int(100 / korova)):
        for t in range(1, int(100 / telenok)):
            if equation(b, k, t):
                print(b, k, t)