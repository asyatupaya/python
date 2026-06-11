side_size = 8

is_white = True
for i in range(side_size):
    for j in range(side_size):
        print('W' if is_white else 'B', end='\t')
        is_white = not is_white
    print('')
    is_white = not is_white
