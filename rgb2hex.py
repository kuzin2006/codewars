def rgb(r, g, b):
    def corect(val):
        if val < 0:
            return 0
        elif val > 255:
            return 255
        else:
            return val

    return "".join(["{:0>2}".format(hex(i)[2:].upper()) for i in [corect(i) for i in [r, g, b]]])


print(rgb(1,2,3))