def is_pal_check_v1(text):
    if not text.isspace():
        text_simpl = text.lower().replace(' ', '')
        char_list = list(text_simpl)
        for i in range(len(char_list) // 2):
            if char_list[i] != char_list[-i-1]:
                return False
    else:
        return False

    return True

def is_pal_check_v2(text):
    if not text.isspace():
        text_simpl = text.lower().replace(' ', '')
#        len_half = len(text_simpl) // 2
#        text_half = text_simpl[:len_half]
#        text_half_rev = text_simpl[:len_half:-1]
#        if text_half != text_half_rev:
        if text_simpl[:] != text_simpl[::-1]:
            return False
    else:
        return False

    return True


while True:
    text = input("Enter the text to analyze, please (empty string to exit): ")
    if text == "":
        exit(0)
    if is_pal_check_v1(text) and is_pal_check_v2(text):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")