import sys
from collections import deque

width, height = map(int, sys.stdin.readline().split())
box = []
box.append([-1] * (width + 2))
for _ in range(height):
    box.append([-1] + list(map(int, sys.stdin.readline().strip('\n').split())) + [-1])
box.append([-1] * (width + 2))

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

starting_spot = []
counting_ripe = 0
counting_space = 0
total = height * width
for y_idx in range(1, height + 1):
    for x_idx in range(1, width + 1):
        if box[y_idx][x_idx] == 1:
            starting_spot.append([y_idx, x_idx, 0])
            counting_ripe += 1
        elif box[y_idx][x_idx] == -1:
            counting_space += 1

all_done = 0

if counting_space + counting_ripe == total:
    print(0)
else:
    progress_que = deque([])
    for element in starting_spot:
        progress_que.append(element)
    while progress_que:
        point = progress_que.popleft()
        if all_done < point[2]:
            all_done = point[2]
        for direction in directions:
            if not box[point[0] + direction[0]][point[1] + direction[1]]:
                box[point[0] + direction[0]][point[1] + direction[1]] = 1
                progress_que.append([point[0] + direction[0], point[1] + direction[1], point[2] + 1])
    is_not_ripe = False
    for y_idx in range(1, height + 1):
        for x_idx in range(1, width + 1):
            if box[y_idx][x_idx] == 0:
                is_not_ripe = True
                break
    if is_not_ripe:
        print(-1)
    else:
        print(all_done)