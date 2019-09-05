# https://www.codewars.com/kata/bird-mountain/train/python


def is_complete(mountain):
    return False if list(filter(lambda x: '^' in x, mountain)) else True


def peak_height(mountain):
    mountain_coords = [list(row) for row in mountain]
    mountain_width = len(mountain[0])
    mountain_height = len(mountain)

    max_height = 0
    while not is_complete(mountain_coords):
        if max_height == 0:
            border = ' '
        else:
            border = max_height
        for r_idx, row in enumerate(mountain_coords):
            for s_idx, symbol in enumerate(row):
                # collect neighbours
                if symbol == '^':
                    neighbours_coords = [(r_idx-1, s_idx),
                                         (r_idx, s_idx+1),
                                         (r_idx+1, s_idx),
                                         (r_idx, s_idx-1)]  # top, right, bottom, left
                    for coord in neighbours_coords:
                        if -1 in coord \
                                or coord[0] >= mountain_height \
                                or coord[1] >= mountain_width\
                                or mountain_coords[coord[0]][coord[1]] == border:  # check if element is on border
                            mountain_coords[r_idx][s_idx] = max_height + 1
                            break
        max_height += 1
    return max_height



mountain = [
          "^^^^^^        ",
          " ^^^^^^^^     ",
          "  ^^^^^^^     ",
          "  ^^^^^       ",
          "  ^^^^^^^^^^^ ",
          "  ^^^^^^      ",
          "  ^^^^        "
        ]

print(peak_height(mountain))