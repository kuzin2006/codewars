# https://www.codewars.com/kata/strip-comments/train/python
import re


def solution(string, markers):
    lines = string.splitlines()
    if not markers:
        return string
    regexp = "[{}]+.*".format(re.escape(''.join(markers)))
    return '\n'.join([re.sub(regexp, '', line).strip() for line in lines])


print(repr(solution('apples bananas lemons avocados bananas bananas\n? strawberries apples watermelons apples\napples\noranges lemons ? strawberries', [',', '#', '-', '@'])))
