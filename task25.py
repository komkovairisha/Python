# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


some_str = 'a a a b c a a d c d d'
some_list = some_str.split()
some_dict = dict()
for i in set(some_list):    
some_dict[i] = some_list.count(i) - 1
for i in range(-1, -len(some_list), -1):
        if some_dict[some_list[i]] != 0:
                    key = some_list[i}
                    some_list[i] += '_' + str(some_dict[some_list[i]])        
some_dict[key] -= 1
print(' '.join(some_list))