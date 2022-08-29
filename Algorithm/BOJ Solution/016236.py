import sys
from collections import deque

width = int(sys.stdin.readline())
matrix = []
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(width):
    matrix.append(list(map(int, sys.stdin.readline().rstrip('\n'))))

fish = 0
fish_data = []
for y_idx in range(width):
    for x_idx in range(width):
        if str(matrix[y_idx][x_idx]) in '123456':
            fish_data.append([y_idx, x_idx], matrix[y_idx][x_idx])
            fish += 1
        elif matrix[y_idx][x_idx] == 9:
            start_point = [y_idx, x_idx]

if fish == 0:
    print(0)
else:
    size = 2
    time = 0
    level_up = 0
    while True:
        distance = []
        for datum in fish_data:
            distance.append(start_point[0] - datum[0][0])