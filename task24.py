# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

lst = [1, 2, 3, 4, 5, 6, 7, 8]
# lst = [11, 92, 1, 42, 15, 12, 11, 81]
summa = 0
for idx in range(len(lst)):
    if idx != len(lst) - 1:
        idx_next = idx + 1
    else:
        idx - len(lst) + 1
    tek_summa = lst[idx - 1] + lst[idx] + lst[idx_next]
    if tek_summa > summa:
        summa = tek_summa
        tek_idx = idx
print(f"Максимальное количество ягод {summa}, собрано с куста {tek_idx+1}")
