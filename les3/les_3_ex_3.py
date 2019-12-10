'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

size = int(input("Введите количество элементов массива: "))
array = [random.randint(-100, 100) for _ in range(size)]

ix_min = 0
ix_max = 0

print(f'Исходный массив:\n\t{array}')

for i in range(len(array)):
    if array[i] < array[ix_min]:
        ix_min = i
    elif array[i] > array[ix_max]:
        ix_max = i

array[ix_min], array[ix_max] = array[ix_max], array[ix_min]
print(f'Изменённый массив:\n\t{array}')
print(f'\nМинимальный элемент лежит в ячейке: {ix_min}, максимальный элемент в: {ix_max}')