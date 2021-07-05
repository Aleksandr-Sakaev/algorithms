""" 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде
функции. По возможности доработайте алгоритм (сделайте его умнее)."""
import random

list_1 = [random.randint(-100, 100) for i in range(10)]
print(f'Исходный список :\n{list_1}')


def bubble_sort(list_1):
    n = 1

    while n < len(list_1):
        sorted_ = True  # Цикл завершается, если замен больше не происходит

        for i in range(len(list_1) - n):

            if list_1[i] < list_1[i + 1]:
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
                sorted_ = False

        if sorted_ == True:
            break

        n += 1

    print(f'Новый список:\n{list_1}')


bubble_sort(list_1)
