def parse(data):
    result = []
    val = 0
    for char in data:
        if char == 'i':
            val += 1
        elif char == 'd':
            val -= 1
        elif char == 's':
            val *= val
        elif char == 'o':
           result.append(val)
    return result

print(parse("ooo"))