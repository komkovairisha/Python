# 31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(2, 10):
    list_1.append(fib(i - 2))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

n = int(input("введите число:  "))

print(list_1[n-1])