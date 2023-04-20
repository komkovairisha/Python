# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

splitters = [',', '.', '(', ')', '!', '[', ']', '\n']
some_text = str("She sells sea shells on the sea shore The shells\n" +
                "that she sells are sea shells I'm sure.So if she sells sea\n"
                "shells on the sea shore I'm sure that the shells are sea\n"
                                                          " shore shells")
for i in splitters:
        some_text = some_text.replace(i, ' ')
        while '  ' in some_text:
                some_text = some_text.replace('  ', ' ')
some_text = some_text.lower()
result_set = set(some_text.split())
print(result_set)
print(len(result_set))