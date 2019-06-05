def is_isogram(string):
    letters = ""
    for c in string.lower():
        letters += c if c not in letters else ''
    return string.lower() == letters


print(is_isogram("abA"))