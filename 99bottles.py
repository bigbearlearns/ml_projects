def sing(num_bottles):
    for num in range(num_bottles, 0, -1):
        print(num, 'bottles of beer on the wall,', num, 'bottles of beer.')
        print('Take one down and pass it around, ', num - 1, 'bottles of beer on the wall.')



sing(99)
