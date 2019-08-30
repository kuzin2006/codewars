# https://www.codewars.com/kata/count-ip-addresses/train/python


def ip2bin(ip):
    ip_numeric = int(''.join([f"{str(bin(int(i)))[2:]:0>8}" for i in ip.split('.')]), base=2)
    return ip_numeric

def ips_between(start, end):
    return ip2bin(end) - ip2bin(start)


ips_between("10.0.0.0", "10.0.0.50")
