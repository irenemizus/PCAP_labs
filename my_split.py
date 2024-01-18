def mysplit(strng):
    list_words = []
    word = []
    ch_indx = -1
    for ch in strng:
        ch_indx += 1
        if not ch.isspace():
            word.append(ch)
        if word and (ch.isspace() or ch_indx == len(strng) - 1):
            list_words.append(''.join(word))
            word = []
    return list_words


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
