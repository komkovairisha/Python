# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя
# Пример:
# 2   2
#     4

# Ответ:
# def sum(a, b):
#     if b == 0:
#         return a
#     return sum(a+1, b-1)

a = int(input("введите первое число:  "))
b = int(input("введите второе число:  "))
 
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
print("сумма чисел равна: ", sum(a, b))
