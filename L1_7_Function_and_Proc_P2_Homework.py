# Функции часть 2. Домашнее задание.
# Задача 1. Напишите программу на Python для поочередного сложения
# элементов двух заданных списков, используя map и lambda.

print('Task1 - sum of 2 lists')
lst1 = [int(s) for s in input("введите числа для сложения в список1: ").split()]
lst2 = [int(s) for s in input("введите числа для сложения в список2: ").split()]

result = map(lambda x, y: x + y, lst1, lst2)
print(f'сумма списков: {list(result)}')

# Задача 2. Напишите программу на Python для поиска чисел из списка,
# кратных девятнадцати или тринадцати, используя filter и Lambda.

print('Task2 - sum of 2 lists')
lst1 = [int(s) for s in input("введите список чисел: ").split()]

check_if_devided = lambda x: x % 13 == 0 or x % 19 == 0

result = filter(check_if_devided, lst1)
print(f' числа кратные 19 или 13: {set(result)}')

# Задача 3. Напишите программу на Python для вычисления наибольшего
# элемента в списке при помощи reduce

from functools import reduce
print('Task3 - Max value in list')
lst1 = [int(s) for s in input("введите список чисел: ").split()]

result = reduce(lambda x, y: max(x, y), lst1)

print(f' максимальное число из списка: {result}')

