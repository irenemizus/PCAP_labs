def read_int(prompt, min, max):
    while True:
        try:
            numb = int(input(prompt))
            assert (numb >= min and numb <= max)
            return numb
        except ValueError:
            print("Error: wrong input")
            continue
        except AssertionError:
            print(f"Error: the value is not within permitted range ({min}..{max})")
            continue


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
