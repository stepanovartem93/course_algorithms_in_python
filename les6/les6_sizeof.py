'''Урок 3, задача 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''
import sys
import random

print('*' * 50)
print(f'Версия Python: {sys.version}, \nВерсия OS: {sys.platform}')
print('*' * 50)

size = int(input("Введите количество элементов массива: "))
array = [random.randint(0, 100) for _ in range(size)]

ix_min = 0
ix_max = 0

for i in range(1, len(array)):
    if array[i] < array[ix_min]:
        ix_min = i
    elif array[i] > array[ix_max]:
        ix_max = i

summa = 0
for i in range(ix_min + 1, ix_max):
    summa += array[i]

print(f'Исходный массив: {array};')
print(f'Минимальное число: {array[ix_min]}; \nМаксимальное число: {array[ix_max]};')
print(f'Сумма: {summa}.')
print('*' * 50)
print('Лёгкая аналитика программы: ')
print(f'Исходный массив занимает {sys.getsizeof(array)} байт' )
print(f'Минимальное число занимает {sys.getsizeof(array[ix_min])} байт')
print(f'Максимальное число занимает {sys.getsizeof(array[ix_max])} байт')
print(f'Сумма занимает {sys.getsizeof(summa)} байт')
