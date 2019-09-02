# https://www.codewars.com/kata/meeting/train/python


def meeting(s):
    names = [name.upper().split(':') for name in s.split(';')]
    names_uniform = [f"({i[1]}, {i[0]})" for i in names]
    return ''.join(sorted(names_uniform))


print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))