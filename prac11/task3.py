def equation(a, b, c, d, e):
    return a**5 + b**5 + c**5 + d**5 == e**5

min_num = 3
max_num = 150

# когда-нибудь я обязательно разберусь в теории Эйлера и оптимизирую этот ужас

exit_flag = False
for a in range(min_num, max_num + 1):
    for b in range(min_num, max_num + 1):
        for c in range(min_num, max_num + 1):
            for d in range(min_num, max_num + 1):
                for e in range(min_num, max_num + 1):
                    if equation(a, b, c, d, e):
                        print('Числа:', a, b, c, d, e)
                        print(f'Сумма: {a + b + c + d + e}')
                        exit_flag = True
                        break
                    else:
                        print(a, b, c, d, e)

    if exit_flag:
        break
