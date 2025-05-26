vowels = ('a','e','i','o','u','A','E','I','O','U')

print('enter sentence')

sentence = input()

words = sentence.split()
words_filtered = []

for word in words:
    if not word.startswith(vowels):
        continue

    words_filtered.append(word)

print(f"number of words (space used as delimiter): {len(words)}\nwords with first vowel: {words_filtered}")
