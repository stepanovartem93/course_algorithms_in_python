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

# def insertion_sort(array):
#     for i in range(1, len(array)):
#         spam = array[i]
#         j = i
#
#         while array[j - 1] > spam and j > 0:
#             array[j] = array[j - 1]
#             j -= 1
#
#             array[j] = spam
#
# insertion_sort(array)
# print(array)

def mergeSort(array):
    # print("Splitting ",array)
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",array)

mergeSort(array)
print(f'Отсортированный слиянием список:\n\t{array}')