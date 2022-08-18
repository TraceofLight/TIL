import sys

length = int(sys.stdin.readline())
matrix = []

for _ in range(length):
    matrix.append(list(map(int, sys.stdin.readline().split())))

result_dict = {-1: 0, 0: 0, 1: 0}
def paper_cut(list, x_idx, y_idx, length):
    global result_dict
    if length == 1:
        point = list[y_idx][x_idx]
        result_dict[point] += 1
    else:
        new_length = length // 3
        list_1 = [list[y_index][x_index] for x_index in range(0, 3) for y_index in range(0, 3)]
        print(list_1)

paper_cut(matrix, 0, 0, 9)