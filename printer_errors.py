def printer_error(s):
    err_count = 0
    for code in list(s):
        if code not in "abcdefghijklmn":
            err_count += 1
    return "{}/{}".format(err_count, len(s))




s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(list(s))
print([c for c in map(chr, range(97, 110))])
print(printer_error(s))
print('x' in ['a','b','c'])