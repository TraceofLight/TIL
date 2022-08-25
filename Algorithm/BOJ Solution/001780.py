import sys

result_dict = {-1: 0, 0: 0, 1: 0}

def paper_cut(list, y_idx, x_idx, length):
    global result_dict
    if length == 1:
        result_dict[list[y_idx][x_idx]] += 1
    else:

        def check_paper(list1, y_idx1, x_idx1, length1):
            if length == 1:
                return list1[y_idx1][x_idx1]
            else:
                initial_value = list1[y_idx1][x_idx1]
                for y in range(y_idx1, y_idx1 + length1):
                    for x in range(x_idx1, x_idx1 + length1):
                        if list1[y][x] != initial_value:
                            return None
                return initial_value

        new_length = length // 3
        starting_point = [[y_index, x_index] 
        for y_index in range(y_idx, y_idx + length, new_length) 
        for x_index in range(x_idx, x_idx + length, new_length)]

        paper_result = check_paper(list, y_idx, x_idx, length)

        if paper_result is not None:
            result_dict[paper_result] += 1
        else:
            for point in starting_point:
                paper_cut(list, point[0], point[1], new_length)


length = int(sys.stdin.readline())
matrix = []

for _ in range(length):
    matrix.append(list(map(int, sys.stdin.readline().split())))

paper_cut(matrix, 0, 0, length)

for value in result_dict.values():
    print(value)