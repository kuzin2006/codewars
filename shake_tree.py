# https://www.codewars.com/kata/nut-farm/train/python


def shake_tree(tree):
    nuts_coords = [1 if i == 'o' else 0 for i in tree[0]]
    tree_crone = [i for i in tree if '|' not in i and 'o' not in i]

    for stage in tree_crone:
        for idx, item in enumerate(stage):
            if nuts_coords[idx]:
                if item == '/':  # bounce left
                    nuts_coords[idx-1] += nuts_coords[idx]
                    nuts_coords[idx] = 0
                elif item == '\\':  # bounce right
                    nuts_coords[idx+1] += nuts_coords[idx]
                    nuts_coords[idx] = 0
                elif item == '_':  # stuck
                    nuts_coords[idx] = 0

    return nuts_coords

tree = [" o o o  ",
        " /    / ",
        "   /    ",
        "  /  /  ",
        "   ||   ",
        "   ||   ",
        "   ||   "]

print(shake_tree(tree))
