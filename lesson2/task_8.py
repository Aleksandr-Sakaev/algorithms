# 8. Посчитать, сколько раз встречается определенная цифра во введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


a = int(input("Введите количество чисел: "))
b = int(input("Цифра, которую необходимо посчитать: "))
count = 0
for i in range(1, a + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == b:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, b))