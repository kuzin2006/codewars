# https://www.codewars.com/kata/roboscript-number-1-implement-syntax-highlighting/train/python
from itertools import groupby

def highlight(code):
    codes = {
        'R': 'green',
        'F': 'pink',
        'L': 'red'
    }

    grouped_code = [(key, len(list(item))) for key, item in groupby(code)]
    number, result = '', ''
    for symbol, length in grouped_code:
        if symbol.isalpha():
            if number:
                result += '<span style="color: orange">{}</span>'.format(number)
                number = ''
            result += '<span style="color: {}">{}</span>'.format(codes[symbol], symbol*length)
        elif symbol.isnumeric():
            number += symbol*length
        else:
            if number:
                result += '<span style="color: orange">{}</span>'.format(number)
                number = ''
            result += symbol*length
    # last char
    if number:
        result += '<span style="color: orange">{}</span>'.format(number)

    return result


print(highlight('RRRRR(F45L3)F2'))