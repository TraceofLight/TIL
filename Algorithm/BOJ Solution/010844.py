import sys

number = int(sys.stdin.readline())
val_list = [0, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def stair_number(val):
    global val_list
    length = len(val_list)
    if val <= length - 1:
        return sum(val_list[val][1 :])
    else :
        for idx in range(length, val + 1):
            val_list.append([0 for _ in range(10)])
            for number in range(0, 10):
                if number == 0:
                    val_list[idx][number] = val_list[idx - 1][number + 1]
                elif number > 0 and number < 9:
                    val_list[idx][number] = val_list[idx - 1][number - 1] + val_list[idx - 1][number + 1]
                elif number == 9:
                    val_list[idx][number] = val_list[idx - 1][number - 1]
        return sum(val_list[val][1 :])


print(stair_number(number) % 1000000000)