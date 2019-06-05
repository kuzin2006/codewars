def int32_to_ip(int32):
    bin_ip = "{:0>32}".format(str(bin(int32))[2:])
    return ".". join([str(int(bin_ip[i*8:i*8+8], 2)) for i in range(0, 4)])

print(int32_to_ip(154959208)) #, "128.114.17.104")
