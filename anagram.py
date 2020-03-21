def list_anagrams(words):
    words_with_sorted_symbols = [(word, "".join(sorted(word))) for word in words]

    hash_dict = {word[1]: {'count': 0, 'words': ''} for word in words_with_sorted_symbols}

    for word in words_with_sorted_symbols:
        if word[1] in hash_dict.keys():
            hash_dict[word[1]]['count'] += 1
            hash_dict[word[1]]['words'] += f'{word[0]}, '

    for value in hash_dict.values():
        if value['count'] > 1:
            print(value['words'])


with open('unixdict.txt', 'r') as file:
    words = [line.replace('\n', '') for line in file]
    list_anagrams(words)

