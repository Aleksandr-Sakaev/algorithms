"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections


def sum_tuple(numbers):
    '''tuple --> sum'''

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Enter = collections.namedtuple('Enter', ['w1', 'w2', 'w3', 'w4'])

base_enter = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    base_enter[name] = Enter(
        w1=profit_q1,
        w2=profit_q2,
        w3=profit_q3,
        w4=profit_q4
    )

general_profit = ()

for name, profit in base_enter.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    general_profit += profit

avg_profit_total = sum(general_profit) / len(base_enter)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_enter.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in base_enter.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')

