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





# Есть предположения что сделаны неверные расчёты
# cProfile.run('find_min_max_1(10)')
# 60 function calls in 0.000 seconds

# python -m timeit -n 10 -s "import task_1" "task_1.find_min_max_1(10)"
# 10 loops, best of 5: 258 usec per loop

# python -m timeit -n 100 -s "import task_1" "task_1.find_min_max_1(10)"
# 100 loops, best of 5: 547 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_1(10)"
# 1000 loops, best of 5: 404 usec per loop

# python -m timeit -n 10000 -s "import task_1" "task_1.find_min_max_1(10)"
# 10000 loops, best of 5: 442 usec per loop

#=========================================================================
# cProfile.run('find_min_max_2(10)')
# 66 function calls in 0.001 seconds

# python -m timeit -n 10 -s "import task_1" "task_1.find_min_max_2(10)"
# 10 loops, best of 5: 210 usec per loop

# python -m timeit -n 100 -s "import task_1" "task_1.find_min_max_2(10)"
# 100 loops, best of 5: 237 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.find_min_max_2(10)"
# 1000 loops, best of 5: 424 usec per loop

# python -m timeit -n 10000 -s "import task_1" "task_1.find_min_max_2(10)"
# 10000 loops, best of 5: 434 usec per loop

#=========================================================================
# cProfile.run('find_min_max_1(100)')
# 534 function calls in 0.001 seconds

# cProfile.run('find_min_max_2(100)')
# 550 function calls in 0.000 seconds

# cProfile.run('find_min_max_1(1000)')
# 5260 function calls in 0.007 seconds

# cProfile.run('find_min_max_2(1000)')
# 5308 function calls in 0.006 seconds

# cProfile.run('find_min_max_1(10000)')
# 52664 function calls in 0.047 seconds

# cProfile.run('find_min_max_2(10000)')
# 52682 function calls in 0.042 seconds

# cProfile.run('find_min_max_1(100000)')
# 527216 function calls in 0.402 seconds

# cProfile.run('find_min_max_2(100000)')
# 527224 function calls in 0.294 seconds

# cProfile.run('find_min_max_1(1000000)')
# 5273063 function calls in 3.117 seconds

# cProfile.run('find_min_max_2(1000000)')
# 5273093 function calls in 2.749 seconds

