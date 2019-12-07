'''4. Определить, какое число в массиве встречается чаще всего.'''

import random


array = [random.randint(-10, 5) for i in range(15)]

num = array[0]
quantity = 1

print(array)

for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
        if spam > quantity:
            quantity = spam
            num = array[i]

if quantity > 1:
    print(f'Число {num} встречается {quantity} раз(а)')
else:
    print("Все числа уникальны")
