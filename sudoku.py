def is_correct(list):
    list_sort = sorted(list)
    for i in range(1, 10):
        if list_sort[i - 1] != str(i):
            return False

    return True

while True:
    print("Input your Sudoku row by row, please")
    table_to_check = []
    for i in range(9):
        table_to_check.append(list(input(f"Row {i + 1}: ")))

    is_correct_row = True
    is_correct_clmn = True
    is_correct_tile = True

    # Making list of columns
    table_to_check_transposed = []
    for col in range(9):
        clmn = []
        for row in table_to_check:
            clmn.append(row[col])
        table_to_check_transposed.append(clmn)

    # Making list of tiles
    table_to_check_tiles = []
    for tr in range(3):
        for tc in range(3):
            tile = []
            for c in range(0, 3):
                for r in range(0, 3):
                    tile.append(table_to_check[tr * 3 + r][tc * 3 + c])
            table_to_check_tiles.append(tile)

    for row in table_to_check:
        if not is_correct(row):
            is_correct_row = False
            print("There is a mistake in your rows!")
            break

    for col in table_to_check_transposed:
        if not is_correct(col):
            is_correct_clmn = False
            print("There is a mistake in your columns!")
            break

    for tile in table_to_check_tiles:
        if not is_correct(tile):
            is_correct_tile = False
            print("There is a mistake in your tiles!")
            break

    if is_correct_row and is_correct_clmn and is_correct_tile:
        print("Your Sudoku is correct!\n")
    else:
        print("Your Sudoku is incorrect!\n")

