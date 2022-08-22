import sys

length_input = int(sys.stdin.readline())
matrix = []

for _ in range(length_input):
    matrix.append(list(map(int, sys.stdin.readline().split())))

counter_0 = 0
counter_1 = 0


def check_color(plane, y_index, x_index, leng):
    for y_idx in range(leng):
        for x_idx in range(leng):
            if not x_idx and not y_idx:
                color = plane[y_index + y_idx][x_index + x_idx]
                continue
            if plane[y_index + y_idx][x_index + x_idx] != color:
                return None
    return color


def cut_paper(paper, start_y, start_x, length):
    global counter_0
    global counter_1
    if length == 1:
        if not paper[start_y][start_x]:
            counter_0 += 1
        else:
            counter_1 += 1
    else:
        half_length = length // 2
        paper_spot = [[start_y, start_x], [start_y, start_x + half_length], 
        [start_y + half_length, start_x], [start_y + half_length, start_x + half_length]]
        check_result = check_color(paper, start_y, start_x, length)
        if check_result == 1:
            counter_1 += 1
        elif check_result == 0:
            counter_0 += 1
        else:
            for spot in paper_spot:
                cut_paper(paper, spot[0], spot[1], half_length)


cut_paper(matrix, 0, 0, length_input)

print(counter_0)
print(counter_1)