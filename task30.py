# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9

a1, d, n = [int(el) for el in input("Введите 3 числа через пробел: первый элемент массива, шаг прогрессии, количество элементов ").split()]


def create_arith_progression(start, step, lenght):
    return [start + step * idx for idx in range(lenght)]


print(create_arith_progression(a1, d, n))
