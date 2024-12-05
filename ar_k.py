def single_root_words(root_word, *other_words):
    same_words = []
    lower_upper_word = root_word.lower().upper()
    for i in other_words:
        if lower_upper_word in i.lower().upper() \
                or i.lower().upper() in lower_upper_word:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
