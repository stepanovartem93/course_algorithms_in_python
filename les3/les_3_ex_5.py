'''В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.'''
import random

array = [random.randint(-100, 100) for i in range(20)]

i = 0
index = -1

while i < len(array):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

print(array)
if index != -1:
    print(f'Максимальное отрицательное число {array[index]}'
          f', находится в ячейке {index}.')
