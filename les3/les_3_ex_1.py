'''1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.'''

array_1 = [i for i in range(2, 100)]
array_2 = [i for i in range(2, 10)]

for i in array_2:
    quantity = 0
    for j in array_1:
        if j % i == 0:
            quantity += 1
    print(f'числу {i} кратно {quantity} чисел')
