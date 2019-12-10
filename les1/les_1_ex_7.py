'''7. Определить, является ли год, который ввел пользователь, високосным или не високосным.'''
import timeit
import cProfile
# year = int(input("введите год: "))

# метод №1
def spot_year_1(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print(f'ваш год {year} - не високосный')
    else:
        print(f'ваш год {year} - високосный')

# метод №2
def spot_year_2(year):
    if year % 4 != 0:
        print(f'ваш год {year} - не високосный')
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f'ваш год {year} - високосный')
        else:
            print(f'ваш год {year} - не високосный')
    else:
        print(f'ваш год {year} - високосный')

cProfile.run("spot_year_2(2036)")