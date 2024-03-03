import os

file = input("Please enter the file name to analyze: ")

char_freq_dict = {}
try:
    fh = open(file, "rt")

    ch = None
    while ch != '':
        ch = fh.read(1).lower()
        if ch not in char_freq_dict.keys():
            char_freq_dict[ch] = 1
        else:
            char_freq_dict[ch] += 1
    fh.close()
except IOError as e:
    print("An I/O problem occured during working with the file \"" + file + "\". Error message: " + os.strerror(e.errno))

char_freq_dict_sort = dict(sorted(char_freq_dict.items(), key=lambda x: x[1], reverse=True))

try:
    foh = open(file + ".hist", "wt")
    for ch in char_freq_dict_sort.keys():
        foh.write(ch + " -> " + str(char_freq_dict_sort[ch]) + "\n")
    foh.close()
except IOError as e:
    print("An I/O problem occured during working with the file \"" + file + ".hist" + "\". Error message: " + os.strerror(e.errno))

for ch in char_freq_dict_sort.keys():
    print(ch + " -> " + str(char_freq_dict_sort[ch]))

