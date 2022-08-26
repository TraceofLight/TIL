import sys

width = int(sys.stdin.readline())
matrix = []

for _ in range(width):
    matrix.append(list(map(int, sys.stdin.readline().rstrip('\n'))))

fish = 0
for y_idx in range(width):
    for x_idx in range(width):
        if str(matrix[y_idx][x_idx]) in '123456':
            fish += 1
        elif matrix[y_idx][x_idx] == 9:
            start_point = [y_idx, x_idx]

if fish == 0:
    print(0)
else:
    size = 2
    time = 0
    while fish:
        break
