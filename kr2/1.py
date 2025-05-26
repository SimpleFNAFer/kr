def unique_words(text: str):
    words_set = {}
    words = text.split()
    result = []

    for word in words:
        if word not in words_set:
            words_set[word] = 1
            result.append(word)

    return result


print('enter text:')
t = input()
print(f"unique words: {unique_words(t)}")
