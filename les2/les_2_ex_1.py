'''1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.'''

print("Простой калькулятор на Python")
while True:
    oper = input("Введите операцию(/,*,-,+,0 - для выхода), которую хотите выполнить с числами: ")
    if oper == 0:
        break
    if oper == '/' or oper == '*' or oper == '-' or oper == '+':
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        if oper == '/':
            try:
                print(f'{x / y:.2f}')
            except ZeroDivisionError:
                print("На ноль делить нельзя")
        elif oper == '*':
            print(f'{x * y:.2f}')
        elif oper == '-':
            print(f'{x - y:.2f}')
        elif oper == '+':
            print(f'{x + y:.2f}')
    else:
        print("Неверный знак операции")