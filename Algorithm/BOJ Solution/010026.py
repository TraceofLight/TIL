from re import L
import sys

#color_weekness

line_number = int(sys.stdin.readline().rstrip('\n'))
matrix = []

for _ in range(line_number):
    matrix.append(list(sys.stdin.readline()))

visited_normal = [[False for _ in range(line_number)] for _ in range(line_number)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
area_normal = 0
progress_stack = []

for y_idx in range(line_number):
    for x_idx in range(line_number):
        if not visited_normal[y_idx][x_idx]:
            visited_normal[y_idx][x_idx] = True
            progress_stack.append([y_idx, x_idx])
            while progress_stack:
                new_spot = progress_stack.pop()
                visited_normal[new_spot[0]][new_spot[1]] = True
                for direction in directions:
                    wide_area = [new_spot[0] + direction[0], new_spot[1] + direction[1]]
                    if (wide_area[0] >= 0 and wide_area[0] < line_number
                        and wide_area[1] >= 0 and wide_area[1] < line_number):
                        if not visited_normal[wide_area[0]][wide_area[1]]:
                            if matrix[new_spot[0]][new_spot[1]] == matrix[wide_area[0]][wide_area[1]]:
                                progress_stack.append(wide_area)
            area_normal += 1
        else:
            continue

visited_weakness = [[False for _ in range(line_number)] for _ in range(line_number)]
area_weakness = 0

for y in range(line_number):
    for x in range(line_number):
        if matrix[y][x] == 'R':
            matrix[y][x] = 'G'

for y_idx in range(line_number):
    for x_idx in range(line_number):
        if not visited_weakness[y_idx][x_idx]:
            visited_weakness[y_idx][x_idx] = True
            progress_stack.append([y_idx, x_idx])
            while progress_stack:
                new_spot = progress_stack.pop()
                visited_weakness[new_spot[0]][new_spot[1]] = True
                for direction in directions:
                    wide_area = [new_spot[0] + direction[0], new_spot[1] + direction[1]]
                    if (wide_area[0] >= 0 and wide_area[0] < line_number
                        and wide_area[1] >= 0 and wide_area[1] < line_number):
                        if not visited_weakness[wide_area[0]][wide_area[1]]:
                            if matrix[new_spot[0]][new_spot[1]] == matrix[wide_area[0]][wide_area[1]]:
                                progress_stack.append(wide_area)
            area_weakness += 1
        else:
            continue

print(area_normal, area_weakness)