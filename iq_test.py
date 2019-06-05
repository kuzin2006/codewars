def iq_test(numbers):
    numbers_even = [int(i) for i in numbers.split(" ") if int(i) % 2 == 0]
    numbers_odd = [int(i) for i in numbers.split(" ") if int(i) % 2 != 0]
    return [int(i) for i in numbers.split(" ")] \
                .index((numbers_odd, numbers_even)[len(numbers_odd) > len(numbers_even)][0])+1


print(iq_test("2 4 7 8 10"))
