'''1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.'''
from collections import  namedtuple

size = int(input("Введите количество предприятий: "))

companies = namedtuple('companies', ['q1', 'q2', 'q3', 'q4'])
main_companies = {}

for i in range(size):
    company = input("Название для " + str(i+1) + '-го предприятия: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    main_companies[company] = companies(
        q1 = profit_q1,
        q2 = profit_q2,
        q3 = profit_q3,
        q4 = profit_q4
    )

total_profit = ()

for name, profit in main_companies.items():
    print(f'Предприятие: {company} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(main_companies)
print(f'\nСредняя прибыль за год для всех предприятий {avg_profit_total}')

print('\nПредприятия, у которых прибыль выше среднего:')

for name, profit in main_companies.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

print('\nПредприятия, у которых прибыль ниже среднего:')

for name, profit in main_companies.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')