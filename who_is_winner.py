from numpy import diagonal, fliplr


def who_is_winner(pieces_position_list):
    # check line of symbols for the winner
    # return R Y or False
    # len of line 4+ symbols
    def check_line(line):
        if len(line) < 4:
            return False
        counter = 0
        curr_symbol = ''
        for symbol in line:
            if symbol:
                if symbol != curr_symbol:
                    counter = 1
                    curr_symbol = symbol
                else:
                    counter += 1
            else:
                counter = 0
                curr_symbol = ''
            if counter >= 4:
                return curr_symbol
        return False

    # return values
    result = {
        'R': 'Red',
        'Y': 'Yellow'
    }

    # analyze game step by step
    for i in range(len(pieces_position_list)):
        # parse position list
        board = [[], [], [], [], [], [], []]

        for move in pieces_position_list[:i]:
            board[ord(move[0]) - ord('A')].append(move[2])
        # uniform length for all columns
        for item in board:
            length = len(item)
            if length < 6:
                for i in range(6-length):
                    item.append('')

        # collect all possible rows, cols and diagonals
        rows = []

        # verticals
        for line in board:
            rows.append(line)

        # horizontals
        for i in range(6):
            rows.append([val[i] for val in board])

        # up-right diagonals
        for rowStart in range(-3, 4):  # cols iteration, 4+ length diagonals
            rows.append([i for i in diagonal(board, -rowStart)])

        # down-left dagonals
        for rowStart in range(-3, 4):  # cols iteration, 4+ length diagonals
            rows.append([i for i in diagonal(fliplr(board), -rowStart)])

        # debug board
        # print()
        # for item in board:
        #     print([i if i else 'x' for i in item])

        # now check all the stuff
        for row in rows:
            check = check_line(row)
            if check:
                return result[check]

    # nothing found, return Draw
    return 'Draw'


print( who_is_winner([
"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
"B_Yellow", "B_Red"
]))





"""


def fixeds([
"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]):
    Test.assert_equals(who_is_winner(), "Yellow")

    Test.assert_equals(who_is_winner([
"C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
"G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
"D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
"C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
"E_Yellow", "E_Red"
]), "Yellow")

    Test.assert_equals(who_is_winner(), "Red")

    Test.assert_equals(who_is_winner([
"A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
"G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
]), "Red")

    Test.assert_equals(who_is_winner([
"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
]), "Yellow")

    Test.assert_equals(who_is_winner([
"A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
]), "Draw");

"""