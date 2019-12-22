'''Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.'''
# **********************************************************************************************************************
import random

array = [i for i in range(0, 50)]
random.shuffle(array)
print(f'Исходный массив:\n\t{array}')
print('*' * 100)
print(f'max_num = {max(array)}, min_num = {min(array)}')
print('*' * 100)

def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

            array[j] = spam

insertion_sort(array)
print(array)