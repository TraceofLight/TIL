import sys
from collections import deque

height, width = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(height):
    matrix.append(list(sys.stdin.readline().strip()))

is_visited = []
for row in matrix:
    is_visited.append([not int(element) for element in row])

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

progress_que = deque([])
progress_que.append([[0, 0], 1])
is_visited[0][0] = True
while progress_que:
    progress_idx = progress_que.popleft()
    if progress_idx[0] == [height - 1, width - 1]:
        print(progress_idx[1])
        break
    for direction in directions:
        if (progress_idx[0][0] + direction[0] >= 0 and
        progress_idx[0][0] + direction[0] < height and
        progress_idx[0][1] + direction[1] >= 0 and
        progress_idx[0][1] + direction[1] < width):
            if not is_visited[progress_idx[0][0] + direction[0]][progress_idx[0][1] + direction[1]]:
                progress_que.append([[progress_idx[0][0] + direction[0], 
                progress_idx[0][1] + direction[1]], progress_idx[1] + 1])
                is_visited[progress_idx[0][0] + direction[0]][progress_idx[0][1] + direction[1]] = True