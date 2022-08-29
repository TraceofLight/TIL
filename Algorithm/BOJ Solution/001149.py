# DP

import sys

house_number = int(sys.stdin.readline())
cost_list = []
for _ in range(house_number):
    cost_list.append(list(map(int, sys.stdin.readline().split())))

val_list = [[cost_list[0][0], cost_list[0][1], cost_list[0][2]]]

for idx in range(1, house_number):
    val_list.append([min(val_list[idx - 1][1] + cost_list[idx][0], val_list[idx - 1][2] + cost_list[idx][0]),
                    min(val_list[idx - 1][0] + cost_list[idx][1], val_list[idx - 1][2] + cost_list[idx][1]),
                    min(val_list[idx - 1][0] + cost_list[idx][2], val_list[idx - 1][1] + cost_list[idx][2])])

print(min(val_list[house_number - 1]))

'''
# BFS를 통한 문제 풀이 - 시간 초과

import sys
from collections import deque

house_number = int(sys.stdin.readline())l
cost_list = []
for _ in range(house_number):
    cost_list.append(list(map(int, sys.stdin.readline().split())))

progress_que = deque([])
for idx in range(3):
    progress_que.append([1, idx, cost_list[0][idx]])

result = float('inf')
color_list = [0, 1, 2]

while progress_que:
    now_index = progress_que.popleft()
    if now_index[0] == house_number:
        if result > now_index[2]:
            result = now_index[2]
    elif now_index[2] > result:
        continue
    else:
        for number in color_list:
            if number == now_index[1]:
                continue
            else:
                progress_que.append([now_index[0] + 1, number, 
                now_index[2] + cost_list[now_index[0]][number]])

print(result)
'''
