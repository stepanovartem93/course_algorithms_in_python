'''6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''

import random

size = int(input("Введите количество элементов массива: "))
array = [random.randint(0, 100) for _ in range(size)]

ix_min = 0
ix_max = 0

print(f'Исходный массив: {array}')
for i in range(1, len(array)):
    if array[i] < array[ix_min]:
        ix_min = i
    elif array[i] > array[ix_max]:
        ix_max = i

if ix_min > ix_max:
    array[ix_min],array[ix_max] = array[ix_max], array[ix_min]

print(f'Минимальное число: {array[ix_min]}, \nМаксимальное число: {array[ix_max]}')

summa = 0
for i in range(ix_min + 1, ix_max):
    summa += array[i]

print(f'Сумма: {summa}')