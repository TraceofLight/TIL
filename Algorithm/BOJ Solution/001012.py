import sys

testcase = int(sys.stdin.readline())
output = []

for case in range(testcase):
    width, height, amount = list(map(int, sys.stdin.readline().split()))
    matrix = [[0 for _ in range(width)] for _ in range(height)]
    for cabbage in range(amount):
        idx_x, idx_y = list(map(int, sys.stdin.readline().split()))
        matrix[idx_y][idx_x] = 1

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    total_cabbage = amount
    combine_cabbage = 0

    for idx_y in range(height):
        for idx_x in range(width):
            for direction in directions:
                if idx_y + direction[0] >= 0 and idx_y + direction[0] < height and idx_x + direction[1] >= 0 and idx_x + direction[1] < width:
                    if matrix[idx_y + direction[0]][idx_x + direction[1]] == 1 and matrix[idx_y][idx_x] == 1:
                        combine_cabbage += 1
                        break
                else:
                    continue
    output.append(total_cabbage - combine_cabbage / 2)

print(*output, sep='\n')