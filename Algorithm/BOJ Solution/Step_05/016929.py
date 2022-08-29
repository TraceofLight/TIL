import sys

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

height, width = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(height):
    matrix.append(list(sys.stdin.readline().rstrip('\n')))

is_got_answer = False
progress_stack = []

for y_idx in range(1, height):
    for x_idx in range(1, width):
        progress_stack.append([[y_idx, x_idx],[[y_idx, x_idx]], 1])
        start_color = matrix[y_idx][x_idx]
        while progress_stack:
            now_idx = progress_stack.pop()
            for direction in directions:
                new_y = now_idx[0][0] + direction[0]
                new_x = now_idx[0][1] + direction[1]
                if (new_y >= 0 and new_y < height 
                and new_x >= 0 and new_x < width):
                    if matrix[new_y][new_x] == start_color:
                        if [new_y, new_x] not in now_idx[1]:
                            progress_stack.append([[new_y, new_x], now_idx[1] + [[new_y, new_x]], now_idx[2] + 1])
                        elif [new_y, new_x] == [y_idx, x_idx] and now_idx[2] + 1 >= 4:
                            is_got_answer = True
                            break
            if is_got_answer:
                break
        if is_got_answer:
            break
    if is_got_answer:
        break

if is_got_answer:
    print('Yes')
else:
    print('No')

'''
# 문제 잘못 이해한 풀이

import sys

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

height, width = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(height):
    matrix.append(list(sys.stdin.readline().rstrip('\n')))

is_got_answer = False
progress_stack = []

for y_idx in range(height - 1):
    for x_idx in range(width - 1):
        print(y_idx, x_idx)
        progress_stack.append([[y_idx, x_idx], 0])
        start_color = matrix[y_idx][x_idx]
        while progress_stack:
            print(progress_stack)
            now_idx = progress_stack.pop()
            if now_idx[1] == 0:
                if now_idx[0][0] + directions[0][0] >= 0 and now_idx[0][0] + directions[0][0] < height:
                    if matrix[now_idx[0][0] + directions[0][0]][now_idx[0][1] + directions[0][1]] == start_color:
                        progress_stack.append([[now_idx[0][0] + directions[0][0], now_idx[0][1] + directions[0][1]], 0])
                if now_idx[0][1] + directions[1][1] >= 0 and now_idx[0][1] + directions[1][1] < width and now_idx[0][0] != y_idx:
                    if matrix[now_idx[0][0] + directions[1][0]][now_idx[0][1] + directions[1][1]] == start_color:
                        progress_stack.append([[now_idx[0][0] + directions[1][0], now_idx[0][1] + directions[1][1]], 1])
            elif now_idx[1] == 1:
                if now_idx[0][1] + directions[1][0] >= 0 and now_idx[0][1] + directions[1][1] < width:
                    if matrix[now_idx[0][0] + directions[1][0]][now_idx[0][1] + directions[1][1]] == start_color:
                        progress_stack.append([[now_idx[0][0] + directions[1][0], now_idx[0][1] + directions[1][1]], 1])
                if matrix[now_idx[0][0] + directions[2][0]][now_idx[0][1] + directions[2][1]] == start_color:
                    progress_stack.append([[now_idx[0][0] + directions[2][0], now_idx[0][1] + directions[2][1]], 2])
            elif now_idx[1] == 2:
                if now_idx[0][0] != y_idx:
                    if matrix[now_idx[0][0] + directions[2][0]][now_idx[0][1] + directions[2][1]] == start_color:
                        progress_stack.append([[now_idx[0][0] + directions[2][0], now_idx[0][1] + directions[2][1]], 2])
                else:
                    if matrix[now_idx[0][0] + directions[3][0]][now_idx[0][1] + directions[3][1]] == start_color:
                        progress_stack.append([[now_idx[0][0] + directions[3][0], now_idx[0][1] + directions[3][1]], 3])
            elif now_idx[1] == 3:
                if now_idx[0][1] != x_idx:
                    if matrix[now_idx[0][0] + directions[3][0]][now_idx[0][1] + directions[3][1]] == start_color:
                        progress_stack.append([[now_idx[0][0] + directions[3][0], now_idx[0][1] + directions[3][1]], 3])
                else:
                    if now_idx[0] == [y_idx, x_idx]:
                        is_got_answer = True
                        break
        if is_got_answer:
            break
    if is_got_answer:
        break

if is_got_answer:
    print('Yes')
else:
    print('No')
'''
