# Задача 36. Дополнительно. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):

    table = '\n'.join(
        map(lambda i: ''.join(
            [f'{operation(i, j):5}' if j != 1 and i != 1 else f'{i:5}'
             if j == 1 else f'{j:5}' for j in range(1, num_columns + 1)]),
            range(1, num_rows + 1)))
    print(table)


rows, columns = [int(x) for x in input(
    'Введите количество строк и столбцов через пробел: ').split()[:2]]

print()
print_operation_table(lambda x, y: x * y, rows, columns)
print()
print_operation_table(lambda x, y: x/y, rows, columns)
print()
print_operation_table(lambda x, y: x**y, rows, columns)
print()
print_operation_table(lambda x, y: x+y, rows, columns)
print()
print_operation_table(lambda x, y: x-y, rows, columns)