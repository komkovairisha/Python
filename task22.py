# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

N = abs(int(input('Введите количество элементов для первого набора чисел: ')))
A_entered = input("Введите через пробел целые числа - элементы первого набора: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('количество элементов не соответствуют заданному выше')
M = abs(int(input('Введите количество элементов для второго набора чисел: ')))
B_entered = input("Введите через пробел целые числа - элементы второго набора: ").split()
B_num = list(map(int, B_entered))
if len(B_num) != M or M == 0:
    print('количество элементов не соответствуют заданному выше, начните сначала ')
result_lst = set(A_num).intersection(set(B_num))
if len(result_lst) != 0:
    for i in sorted(list(result_lst)):
        print(i, end=" ")
else:
    print("Повторяющихся чисел нет")

