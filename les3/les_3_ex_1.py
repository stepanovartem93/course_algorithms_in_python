'''1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.'''

array = [ar for ar in range(2, 100)]
number = [n for n in range(2, 10)]
quantity = 0

for n in number:
    for ar in array:
        if ar % n == 0:
            quantity += 1
            if n == n + 1:
                print(f'числу {n} кратно {quantity} цифр')
