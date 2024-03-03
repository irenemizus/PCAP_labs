def is_anag_check(str1, str2):
    if not str1.isspace() and not str2.isspace():
        str1_simpl = str1.lower().replace(' ', '')
        str2_simpl = str2.lower().replace(' ', '')

        char_list_1 = list(str1_simpl)
        ch_list_1_sort = sorted(char_list_1)
        char_list_2 = list(str2_simpl)
        ch_list_2_sort = sorted(char_list_2)
#        str1_sort = ''.join(ch_list_1_sort)
#        str2_sort = ''.join(ch_list_2_sort)
#        if str1_sort != str2_sort:
        if ch_list_1_sort != ch_list_2_sort:
            return False
    else:
        return False

    return True


while True:
    str1 = input("Enter the first string to compare, please (empty string to exit): ")
    if str1 == "":
        exit(0)

    str2 = input("Enter the second string to compare, please: ")

    if is_anag_check(str1, str2):
        print("Anagrams")
    else:
        print("Not anagrams")