import sys

dice_number = int(sys.stdin.readline())
dice_list = []

for _ in range(dice_number):
    dice_list.append(list(map(int, sys.stdin.readline().split())))

for dice in dice_list:
    sum_1 = (dice[0] + dice[5])
    sum_2 = (dice[1] + dice[3])
    sum_3 = (dice[2] + dice[4])
    if min(sum_1, sum_2. sum_3) == sum_1:
        pass
