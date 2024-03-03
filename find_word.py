# def is_found(word_list, string):
#     indx_prev = -1
#     for ch in word_list:
#         indx = string.find(ch, indx_prev + 1)
#         if indx < 0:
#             return False
#         else:
#             indx_prev = indx
#
#     return True


while True:
    word_to_search = input("Enter the word to search (empty string to exit): ").lower()
    if word_to_search == "":
        exit(0)

    string_to_search = input("Enter a string to search in: ").lower()

    #word_as_list = list(word_to_search)
    #print("Yes" if is_found(word_as_list, string_to_search) else "No")

    print("Yes" if string_to_search.find(word_to_search) > 0 else "No")
