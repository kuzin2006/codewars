# https://www.codewars.com/kata/nut-farm-2/train/python


def shake_tree(tree):
    nuts_coords = [0] * len(tree[0])
    tree_crone = [i for i in tree if '|' not in i]

    for stage in tree_crone:
        for idx, item in enumerate(stage):
            if item == 'o':  # new nut found
                nuts_coords[idx] += 1
            elif nuts_coords[idx]:
                if item == '/':  # bounce left
                    offset = 0
                    while stage[idx-offset] == '/':
                        offset += 1
                        if stage[idx-offset] == '\\':  # oops, stuck
                            offset = 0
                            nuts_coords[idx] = 0
                            break
                    nuts_coords[idx-offset] += nuts_coords[idx]
                    nuts_coords[idx] = 0
                elif item == '\\':  # bounce right
                    offset = 0
                    while stage[idx + offset] == '\\':
                        offset += 1
                        if stage[idx+offset] == '/':  # oops, stuck
                            offset = 0
                            nuts_coords[idx] = 0
                            break
                    nuts_coords[idx+offset] += nuts_coords[idx]
                    nuts_coords[idx] = 0
                elif item == '_':  # stuck
                    nuts_coords[idx] = 0

    return nuts_coords

tree = [" oooooo ",
        " oooooo ",
        " oooooo ",
        " oooooo ",
        " oooooo ",
        " \\////\\ ",
        "   ||   ",
        "   ||   ",
        "   ||   "]

print(shake_tree(tree))
