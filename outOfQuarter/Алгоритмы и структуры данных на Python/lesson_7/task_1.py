# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

def sort(arr):
    n = 1
    while n < len(arr)-1:
        item = False
        for i in range(len(arr)-n):
            if  arr[i] < arr[i+1]:# Перестановка на убывание
                arr[i], arr[i+1] = arr[i+1], arr[i]
                item  = True
        if not item: #Оптимизация : выход из массива если за проход небыло перестановок
            print(f'Длина массива {len(arr)}, количество проходов {n}')
            print('*'*50)
            print(arr)
            break
        n += 1

sort([random.randint(-100, 100) for _ in range(15)])