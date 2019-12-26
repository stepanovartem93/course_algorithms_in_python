

M = 5
N = 4
matrix = []

for i in range(N):
    row = []
    summ = 0

    for j in range(M - 1):
        num = int(input(f'Строка {i}, элемент {j}: '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()