def sum_dig(numb):
    sum = numb
    while len(str(sum)) > 1:
        inp_dig_list = [ int(d) for d in list(str(sum)) ]
        sum = 0
        for d in inp_dig_list:
            sum += d
    return sum

while True:
    date = input("Enter your date of birth (in any of the following formats: YYYYMMDD, YYYYDDMM, or MMDDYYYY); empty string to exit: ")
    if date == "":
        exit(0)
    try:
        inp_numb = int(date)
    except:
        print("The date you entered is incorrect!")
        continue

    print(sum_dig(inp_numb))