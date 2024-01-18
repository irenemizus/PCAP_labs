# Digit patterns
ONE = (' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#')
TWO = ('#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#')
THREE = ('#', '#', '#', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#')
FOUR = ('#', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', '#')
FIVE = ('#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#')
SIX = ('#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#')
SEVEN = ('#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#')
EIGHT = ('#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#')
NINE = ('#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#')
ZERO = ('#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#')

dig_list = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]


def show_digit(dig):
    dig_lines = []
    show_dig = dig_list[dig]
    for i in range(0, len(show_dig), 3):
        dig_line = ''.join(show_dig[i:i + 3])
        dig_lines.append(dig_line)
        #print(dig_line)
    return dig_lines


def show_number(numb):
    dig_lines_list = []
    numb_str = str(numb)
    for d in numb_str:
        dig = int(d)
        dig_lines_list.append(show_digit(dig))

    for numb_line in range(5):
        print(' '.join([ dl[numb_line] for dl in dig_lines_list ]))


show_number(9081726354)