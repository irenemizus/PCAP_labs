# Caesar cipher.
while True:
    text = input("Enter your message (empty string to exit): ")
    if text == "":
        exit(0)
    shift_txt = input("Enter a shift value (an integer number from the range 1..25): ")
    try:
        shift = int(shift_txt)
    except:
        print("The entered value " + shift_txt + " of the shift is wrong!")
        continue

    if shift < 1 or shift > 25:
        print("The shift value must be in the range 1..25! You've entered the value " + shift_txt)
        continue

    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
        else:
            code = ord(char) + shift
            if char.isupper():
                if code > ord('Z'):
                    code -= ord('Z') - ord('A') + 1
            else:
                if code > ord('z'):
                    code -= ord('z') - ord('a') + 1
            cipher += chr(code)

    print(cipher)
