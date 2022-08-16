import sys

stair_number = int(sys.stdin.readline())
stairs = []
for _ in range(stair_number):
    stairs.append(int(sys.stdin.readline()))


def stair_score(goal):
    global stairs
    max_list = [[0, 0], [stairs[0], stairs[0]]]
    length = len(max_list)
    if goal <= length - 1:
        return max(max_list[goal])
    else:
        for idx in range(length, goal + 1):
            option_a = stairs[idx - 1] + max_list[idx - 1][1]
            option_b = stairs[idx - 1] + max(max_list[idx - 2])
            max_list.append([option_a, option_b])
        return max(max_list[goal])

if stair_number == 0:
    print(0)
else:
    print(stair_score(stair_number))
