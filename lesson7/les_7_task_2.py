""" Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""
import random

array = [round(random.uniform(0, 50), 2) for i in range(10)]

print('Исхоный массив:', array, sep='\n')


def sort_(arr):
    def merge(first, second):
        lst = []
        i, j = 0, 0

        while i < len(first) and j < len(second):

            if first[i] < second[j]:
                lst.append(first[i])
                i += 1

            else:
                lst.append(second[j])
                j += 1

        lst.extend(first[i:] if i < len(first) else second[j:])

        return lst

    def d_half(lst_1):

        if len(lst_1) == 1:
            return lst_1

        elif len(lst_1) == 2:
            return lst_1 if lst_1[0] <= lst_1[1] else lst_1[::-1]

        else:
            return merge(d_half(lst_1[:len(lst_1) // 2]), d_half(lst_1[len(lst_1) // 2:]))

    return d_half(arr)


print('Массив после сортировки:', sort_(array), sep='\n')