# '''задача разложить элементы массива на два массива, массив с эелементами меньше нуля и
# массив с элементами больше нуля'''
# import random
#
# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
#
# arr_below = []
# arr_above = []
#
# for item in array:
#
#     if item > 0:
#         arr_above.append(item)
#     elif item < 0:
#         arr_below.append(item)
#
# print(arr_below)
# print(arr_above)

# '''вставка элемента в произвольное место массива'''
# '''метод 1'''
# import random
#
# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
# #
# num = int(input("Введите целое число для вставки: "))
# pos = int(input("На какую позицию вставить число: "))
#
# array.append(None) # Вставляем в конец массива пустую клетку
# i = len(array) - 1
#
# while i > pos:
#     array[i], array[i - 1] = array [i - 1], array [i]
#     i -= 1
#
# array[pos] = num
# print(array)
#
# '''метод 2'''
# array[pos] = num
# print(array)

# '''Программа создаём матрицу 5 * 7'''
# import random
# matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
# for line in matrix: # перебираем в матрцие каждкую строчку
#     for item in line:  # перебираем в матрице отдельный элемент
#         print(f'{item:>4}', end='') # вывод каждого элемента в формате отступ на 4 знака, при этом
#     print()

# '''Программа подсчитывает сумму строк и столбцов в матрице и выводит на экран результат'''
# import random
# matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
# for line in matrix: # перебираем в матрцие каждкую строчку
#     for item in line:  # перебираем в матрице отдельный элемент
#         print(f'{item:>4}', end='') # вывод каждого элемента в формате отступ на 4 знака, при этом
#     print()
#
# sum_column = [0] * len(matrix[0]) # массив, считает сумму по столбцам существующей матрицы
#
# for line in matrix:
#     sum_line = 0
#
#     for i, item in enumerate(line): # благодаря ф-ии enumerate в переменной i будет храниться № столбца, в item значение строки
#         sum_line += item
#         sum_column[i] += item
#
#         print(f'{item:>5}', end='')
#
#     print(f' | {sum_line}')
#
# print('-' * (len(matrix) * 5))
#
# for s in sum_column:
#     print(f'{s:>5}', end='')

'''Обмен значений главное и побочной диагоналей квадратной матрицы'''
import random

size = 5

matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
for line in matrix: # перебираем в матрцие каждкую строчку
    for item in line:  # перебираем в матрице отдельный элемент
        print(f'{item:>4}', end='') # вывод каждого элемента в формате отступ на 4 знака, при этом
    print()

for i in range(size): # в переменных i and j хранятся индексы элементов матрицы
    for j in range(size):
        if i == j:

            spam = matrix[i][j]
            matrix[i][j] = matrix[i][size - 1 - j]
            matrix[i][size - 1 - j] = spam

print('*' * 30)
for line in matrix: # перебираем в матрцие каждкую строчку
    for item in line:  # перебираем в матрице отдельный элемент
        print(f'{item:>4}', end='') # вывод каждого элемента в формате отступ на 4 знака, при этом
    print()