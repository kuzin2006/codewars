# https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n):
    digits = list(reversed(sorted(list(str(n)))))
    iterator = n+1
    while True:
        if list(reversed(sorted(list(str(iterator))))) == digits:
            return iterator
        else:
            if iterator > int(''.join(digits)):
                break
            else:
                iterator += 1

    return -1


print(next_bigger(12))


