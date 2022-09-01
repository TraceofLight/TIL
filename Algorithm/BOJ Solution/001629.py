import sys
from collections import defaultdict

a, b, c = map(int, sys.stdin.readline().split())

def multiple(number, count, sub):
    multiple_dict = defaultdict(int)
    multiple_dict[1] = number % sub
    if count == 1:
        return multiple_dict[1]
    else:
        if multiple_dict.get(count // 2) == None:
            multiple_dict[count // 2] = multiple(number, count // 2, sub)
        if multiple_dict.get(count - count // 2) == None:
            multiple_dict[count - count // 2] = multiple(number, count - count // 2, sub)
        output = multiple_dict[count // 2] * multiple_dict[count - count // 2]
        multiple_dict[count] = output % sub
        return multiple_dict[count]

print(multiple(a, b, c))