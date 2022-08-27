# 구현을 통한 문제 풀이 

'''
# BFS를 통한 문제 풀이 - 시간 초과

import sys
from collections import deque

house_number = int(sys.stdin.readline())
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

'''
# DP : 최소값만 골라서는 불가능한 케이스 존재
import sys

house_number = int(sys.stdin.readline())
cost_list = []
for _ in range(house_number):
    cost_list.append(list(map(int, sys.stdin.readline().split())))


def choose_house(now_position, selection_cost_list):
    list = []
    for element in selection_cost_list:
        if element == now_position:
            continue
        else:
            list.append(element)
    return list


output = float('inf')
color_list = [0, 1, 2]
for idx in range(3):
    counter = 1
    result = cost_list[0][idx]
    last_idx = idx
    while counter <= house_number - 1:
        cost_val = []
        for color_index in choose_house(last_idx, color_list):
            cost_val.append([cost_list[counter][color_index], color_index])
        if cost_val[0][0] <= cost_val[1][0]:
            result += cost_val[0][0]
            last_idx = cost_val[0][1]
        else:
            result += cost_val[1][0]
            last_idx = cost_val[1][1]
        counter += 1
    if result < output:
        output = result

print(output)
'''
