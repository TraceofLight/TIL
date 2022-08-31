# 주사위 쌓기

import sys

# 주사위 갯수 input
dice_number = int(sys.stdin.readline())

# 주사위 숫자 정보 input
dice_list = []
for _ in range(dice_number):
    dice_list.append(list(map(int, sys.stdin.readline().split())))

# DFS 전수 조사
# 맞닿는 면, 옆면 최대값, 횟수 정보 전달
progress_stack = []
progress_stack.append([dice_list[0][0], max(dice_list[0][1], dice_list[0][2], dice_list[0][3],dice_list[0][4]), 1])
progress_stack.append([dice_list[0][1], max(dice_list[0][0], dice_list[0][2], dice_list[0][4],dice_list[0][5]), 1])
progress_stack.append([dice_list[0][2], max(dice_list[0][0], dice_list[0][1], dice_list[0][3],dice_list[0][5]), 1])
progress_stack.append([dice_list[0][3], max(dice_list[0][0], dice_list[0][2], dice_list[0][4],dice_list[0][5]), 1])
progress_stack.append([dice_list[0][4], max(dice_list[0][0], dice_list[0][1], dice_list[0][3],dice_list[0][5]), 1])
progress_stack.append([dice_list[0][5], max(dice_list[0][1], dice_list[0][2], dice_list[0][3],dice_list[0][4]), 1])

# 합 결과값 기본값 생성, 이후 최고값으로 갱신
max_sum = float('-inf')
while progress_stack:
    now_dice = progress_stack.pop()
    # 모든 주사위를 다 사용했을 때
    # 옆면 최고값의 합이 기존 최고값보다 클 경우 갱신
    if now_dice[2] == dice_number:
        if now_dice[1] > max_sum:
            max_sum = now_dice[1]
    # 주사위를 다 쓰기 전
    # 대응하는 반대편 면, 옆면 최대값 합, 횟수 정보 전달
    elif now_dice[2] < dice_number:
        for idx in range(6):
            if dice_list[now_dice[2]][idx] == now_dice[0]:
                if idx == 0:
                    progress_stack.append([dice_list[now_dice[2]][5], now_dice[1] + max(dice_list[now_dice[2]][1], dice_list[now_dice[2]][2], dice_list[now_dice[2]][3],dice_list[now_dice[2]][4]), now_dice[2] + 1])
                elif idx == 1:
                    progress_stack.append([dice_list[now_dice[2]][3], now_dice[1] + max(dice_list[now_dice[2]][0], dice_list[now_dice[2]][2], dice_list[now_dice[2]][4],dice_list[now_dice[2]][5]), now_dice[2] + 1])
                elif idx == 2:
                    progress_stack.append([dice_list[now_dice[2]][4], now_dice[1] + max(dice_list[now_dice[2]][0], dice_list[now_dice[2]][1], dice_list[now_dice[2]][3],dice_list[now_dice[2]][5]), now_dice[2] + 1])
                elif idx == 3:
                    progress_stack.append([dice_list[now_dice[2]][1], now_dice[1] + max(dice_list[now_dice[2]][0], dice_list[now_dice[2]][2], dice_list[now_dice[2]][4],dice_list[now_dice[2]][5]), now_dice[2] + 1])
                elif idx == 4:
                    progress_stack.append([dice_list[now_dice[2]][2], now_dice[1] + max(dice_list[now_dice[2]][0], dice_list[now_dice[2]][1], dice_list[now_dice[2]][3],dice_list[now_dice[2]][5]), now_dice[2] + 1])
                elif idx == 5:
                    progress_stack.append([dice_list[now_dice[2]][0], now_dice[1] + max(dice_list[now_dice[2]][1], dice_list[now_dice[2]][2], dice_list[now_dice[2]][3],dice_list[now_dice[2]][4]), now_dice[2] + 1])

# 최대값 출력
print(max_sum)