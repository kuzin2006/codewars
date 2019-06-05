def find_nb(m):
    res = 0
    i = 1
    while res < m:
        res += (i)**3
        i += 1
    return (-1, i-1)[res == m]


print(find_nb(1071225))
