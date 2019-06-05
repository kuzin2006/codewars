def howmuch(m, n):
    return [["M:{}".format(money), "B:{:d}".format((money-1) // 7), "C:{:d}".format((money-1) // 9)] \
            for money in range(m, n+1) if ((money-1) % 9 == 0) and ((money-2) % 7 == 0) ]

print(howmuch(20000, 20100))

