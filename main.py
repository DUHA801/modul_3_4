from operator import index


def single_root_words(root_word ,*other_words):
    same_words=[]

    t = list(other_words)

    for i in range(len(t)):
        if root_word.upper() in t[i].upper() or t[i].upper() in root_word.upper():
            same_words.append(t[i])
    return (same_words)



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)