import sys
from collections import deque

matrix_length = int(sys.stdin.readline())
matrix = []
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for _ in range(matrix_length):
    matrix.append(list(sys.stdin.readline()))

point_list = []

for y_idx in range(matrix_length):
    for x_idx in range(matrix_length):
        if matrix[y_idx][x_idx] == '1':
            point_list.append([y_idx, x_idx])

length = len(point_list)
connection = [set() for _ in point_list]

for idx1 in range(length):
    for idx2 in range(length):
        if idx1 == idx2:
            continue
        for direction in directions:
            if [point_list[idx1][0] + direction[0], point_list[idx1][1] + direction[1]] == point_list[idx2]:
                connection[idx1].add(idx2)
                connection[idx2].add(idx2)

visited = [False for _ in range(length)]
progress_que = deque([])

complex = 0
apt_list = []
for idx in range(length):
    if visited[idx]:
        continue
    else:
        progress_que.append(idx)
        visited[idx] = True
        apt_num = 1
        while progress_que != deque([]):
            progress_idx = progress_que.popleft()
            for point in connection[progress_idx]:
                if not visited[point]:
                    progress_que.append(point)
                    apt_num += 1
                    visited[point] = True
        apt_list.append(apt_num)
        complex += 1

apt_list = sorted(apt_list)

print(complex)
print(*apt_list, sep='\n')