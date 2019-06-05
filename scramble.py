def scramble(s1, s2):
    # letters and their quantities in string
    def stat(s):
        res = {}
        for letter in set([ltr for ltr in s]):
            res[letter] = s.count(letter)
        return res

    # take letters and num of their occurences in both str's
    stat1 = stat(s1)
    stat2 = stat(s2)

    for ltr, occur in stat2.items():
        # check if letter in array and number of it is sufficient
        if ltr in stat1.keys():
            if occur > stat1[ltr]:
                return False
        else:
            return False
    return True

    # your code here

print(scramble('katase', 'steeak'))