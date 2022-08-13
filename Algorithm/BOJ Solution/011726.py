import sys

number = int(sys.stdin.readline())
val_list = [0, 1, 2]

def tile(val):
    global val_list
    length = len(val_list)
    if val <= length - 1:
        return val_list[val]
    else:
        for idx in range(length, val + 1):
            val_list.append(val_list[idx - 1] + val_list[idx - 2])
        return val_list[val]


print(tile(number) % 10007)