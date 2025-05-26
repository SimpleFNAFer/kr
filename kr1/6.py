import random
import string

# Создание списка слов из букв нижнего регистра
words_num = random.randint(1, 15)
words_list = []
for i in range(words_num):
    word = ''
    word_len = random.randint(5, 20)

    for j in range(word_len):
        word = f"{word}{random.choice(string.ascii_lowercase)}"

    words_list.append(word)

print(f"input words list: {words_list}")

for i in range(len(words_list)):
    words_list[i] = words_list[i].capitalize()

print(f"processed words list: {words_list}")
