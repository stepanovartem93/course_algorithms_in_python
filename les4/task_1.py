'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random
from timeit import timeit
import cProfile

def find_min_max_1(size):
    ix_min = 0
    ix_max = 0
    array = [random.randint(-100, 100) for _ in range(size)]
    for i in range(len(array)):
        if array[i] < array[ix_min]:
            ix_min = i
        elif array[i] > array[ix_max]:
            ix_max = i

    print(f'Исходный массив:\n\t{array}')

    array[ix_min], array[ix_max] = array[ix_max], array[ix_min]
    print(f'Изменённый массив:\n\t{array}')
    print(f'\nМинимальный элемент лежит в ячейке: {ix_min}, максимальный элемент в: {ix_max}')


def find_min_max_2(size):
    array = [random.randint(-100, 100) for _ in range(size)]
    min_num = min(array)
    max_num = max(array)
    ix_min = array.index(min_num)
    ix_max = array.index(max_num)

    print(f'Исходный массив:\n\t{array}')

    array[ix_min], array[ix_max] = array[ix_max], array[ix_min]
    print(f'Изменённый массив:\n\t{array}')
    print(f'\nМинимальный элемент лежит в ячейке: {ix_min}, максимальный элемент в: {ix_max}')

# ===========================================================================
# Оценка скорости работы алгоритма 1 для массивов размерностью 10, 100 и 1000
# ===========================================================================
# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_1(10)"
# 1000 loops, best of 5: 434 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_1(100)"
# 1000 loops, best of 5: 903 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_1(1000)"
# 1000 loops, best of 5: 5.6 msec per loop
# ===========================================================================
# Оценка скорости работы алгоритма 2 для массивов размерностью 10, 100 и 1000
# ===========================================================================
# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_2(10)"
# 1000 loops, best of 5: 430 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_2(100)"
# 1000 loops, best of 5: 887 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_2(1000)"
# 1000 loops, best of 5: 5.34 msec per loop



# cProfile.run('find_min_max_1(1000)')
# 5283 function calls in 0.005 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.002    0.002 task_1.py:10(<listcomp>)
#         1    0.001    0.001    0.005    0.005 task_1.py:7(find_min_max_1)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.002    0.001    0.002    0.001 {built-in method builtins.print}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1274    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('find_min_max_2(1000)')
# 5272 function calls in 0.008 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#      1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.003    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.008    0.008 task_1.py:24(find_min_max_2)
#         1    0.000    0.000    0.003    0.003 task_1.py:25(<listcomp>)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         3    0.004    0.001    0.004    0.001 {built-in method builtins.print}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1260    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
