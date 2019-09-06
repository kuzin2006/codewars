# https://www.codewars.com/kata/snail/train/python

import itertools

def top_row_transpose(arr):
    while arr:
        yield arr[0]
        arr = list(reversed(list(zip(*arr[1:]))))

def snail(snail_map):
    return list(itertools.chain(*top_row_transpose(snail_map)))



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))
