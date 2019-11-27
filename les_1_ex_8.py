'''8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).'''
print("Программа позволяет вывести среднее число среди трех, введённых пользователем, чисел")

print("Введите три числа")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > b and a > c and b > c:
    print(f'{b} - среднее число')
elif a > b and a > c and b < c:
    print(f'{c} - среднее число')
elif a > b and a < c:
    print(f'{a} - среднее число')
elif a < b and a > c:
    print(f'{a} - среднее число')
elif a < b and a < c and b > c:
    print(f'{c} - среднее число')
elif a < b and a < c and b < c:
    print(f'{b} - среднее число')