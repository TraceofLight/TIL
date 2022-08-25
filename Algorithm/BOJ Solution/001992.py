import sys


def quad_tree(matrix, idx_y, idx_x, length):
    if length == 1:
        return matrix[idx_y][idx_x]
    else:
        string = '('
        starting_point = [[idx_y, idx_x], [idx_y, idx_x + length // 2], [idx_y + length // 2, idx_x], 
                          [idx_y + length // 2, idx_x + length // 2]]

        def is_one_color(list, idx_y, idx_x, length):
            initial_color = list[idx_y][idx_x]
            for y_index in range(idx_y, idx_y + length):
                for x_index in range(idx_x, idx_x + length):
                    if initial_color != list[y_index][x_index]:
                        return None
            return initial_color

        for point in starting_point:
            part_color = is_one_color(matrix, point[0], point[1], length // 2)
            if part_color is not None:
                string = string + part_color
            else:
                string = string + quad_tree(matrix, point[0], point[1], length // 2)
        string = string + ')'
        if string == '(0000)':
            string = '0'
        elif string == '(1111)':
            string = '1'
        return string


length = int(sys.stdin.readline().rstrip('\n'))
matrix = []

for _ in range(length):
    matrix.append(list(sys.stdin.readline().rstrip('\n')))

if length == 1:
    print(f'{matrix[0][0]}')
else:
    print(quad_tree(matrix, 0, 0, length))
