# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def find_vowels(str):
    alph = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
    count = 0
    for el in str:
        if el in alph:
            count += 1
    return count


def is_rhyme(func, verse: str):
    lst_s = verse.strip().split()
    tmp1 = map(func, lst_s)
    tmp2 = set(tmp1)
    if len(tmp2) == 1:
        return [" Парам пам-пам"]
    return ["Пам парам"]


print(is_rhyme(find_vowels, "пара-ра-рам рам-пам-папам па-ра-па-да"))
print(is_rhyme(find_vowels, "пум-пу-рум пу-рум-пу рум-пу-рум пум-пу"))
print(is_rhyme(find_vowels, "Пам-па-рам-пу рум со-пи-лки"))
print(is_rhyme(find_vowels,
      "Пум-пу-рум-ка-рам во-пи-лки"))
print(is_rhyme(find_vowels, "Пум-пу-рум пу-пу-рум трам-пам-па"))