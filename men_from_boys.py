# https://www.codewars.com/kata/sort-out-the-men-from-boys-1/python


def men_from_boys(arr):
    return sorted(list(set([i for i in arr if i % 2 == 0]))) + \
           sorted(list(set([i for i in arr if i % 2 != 0])), reverse=True)


print(men_from_boys([7,3,14,17]))
