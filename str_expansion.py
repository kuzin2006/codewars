def string_expansion(s):
    result = ''
    multiplier = 1
    for i in range(len(s)-1):
        if s[i].isdecimal():
            if s[i+1].isalpha():
                multiplier = int(s[i])
        else:
            result += s[i] * multiplier
    if s[-1].isalpha():
        result += s[-1] * multiplier
    return result

print(string_expansion('5M0L8P1'))  # ,'aaabbbccc'
