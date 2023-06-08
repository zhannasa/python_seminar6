# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# import random
list = []
for i in range(10):
    list.append(random.randint(1,100))
print(list)
max_limit = 30 #int(input('Enter the max limit: '))
min_limit = 10 #int(input('Enter the min limit: '))
index = [i for i in range(0, len(list)) if list[i] > min_limit and list[i] < max_limit]
print(index)
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
