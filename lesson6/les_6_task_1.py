"""Тесты выполнены на 64-разрядной Win 10 версии 1803
Python 3.9.0
Задача: Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран"""


from lesson6 import sum_memory


#способ 1
new_num = ''

num = input('Введите число: ')
count = len(num)
k = range(count)

for i in k:
    new_num = new_num + str(int(num) % 10)
    num = int(num) // 10
print(new_num)

sum_member1 = sum_memory.show_size(new_num) + sum_memory.show_size(num) + sum_memory.show_size(count) + sum_memory.show_size(k)
print('В программе задействовано байт памяти: {}'.format(sum_member1))


# Затраты памяти программы:  163
# Переменная:  123456


#способ 2
num = input('Введите число: ')
new_num = num[::-1]
print(new_num)

sum_member2 = sum_memory.show_size(new_num) + sum_memory.show_size(num)
print('В программе задействовано байт памяти: {}'.format(sum_member2))


# Затраты памяти программы:  62
# Переменная:  123456


# способ 3
x = input('Введите число ')
num = int(x)
new_num = 0
while num > 0:
    new_num = new_num * 10 + num % 10
    num = num//10
print(new_num)

sum_member3 = sum_memory.show_size(new_num) + sum_memory.show_size(x)
print(f'В программе задействовано байт памяти: {sum_member3}')


# Затраты памяти программы:  47
# Переменные:  123456

