import sys

length = int(sys.stdin.readline())
matrix_candy = []

for _ in range(length):
    matrix_candy.append(list(sys.stdin.readline().strip()))


def max_length(list):
    max_counter = 1
    counter = 1
    main_chr = '#'
    for letter in list:
        if letter != main_chr:
            main_chr = letter
            if counter > max_counter:
                max_counter = counter
            counter = 1
        else:
            counter += 1
    if counter > max_counter:
        max_counter = counter
    return max_counter


def max_candy(matrix):
    max_length_candy = 0
    for row in matrix:
        if max_length(row) > max_length_candy:
            max_length_candy = max_length(row)
    new_matrix = list(zip(*matrix))
    for column in new_matrix:
        if max_length(column) > max_length_candy:
            max_length_candy = max_length(column)
    return max_length_candy


def change_n_check(spot1_a, spot1_b, spot2_a, spot2_b, matrix_list, result_list):
    matrix_list[spot1_a][spot1_b], matrix_list[spot2_a][spot2_b] = matrix_list[spot2_a][spot2_b], matrix_list[spot1_a][spot1_b]
    result_list.append(max_candy(matrix_list))
    matrix_list[spot1_a][spot1_b], matrix_list[spot2_a][spot2_b] = matrix_list[spot2_a][spot2_b], matrix_list[spot1_a][spot1_b]


max_candy_list = []

for y_idx in range(length):
    for x_idx in range(length):
        if y_idx == length - 1:
            if x_idx == length - 1:
                continue
            else:
                change_n_check(y_idx, x_idx, y_idx, x_idx + 1, matrix_candy, max_candy_list)
        else:
            if x_idx == length - 1:
                change_n_check(y_idx, x_idx, y_idx + 1, x_idx, matrix_candy, max_candy_list)
            else:
                change_n_check(y_idx, x_idx, y_idx, x_idx + 1, matrix_candy, max_candy_list)
                change_n_check(y_idx, x_idx, y_idx + 1, x_idx, matrix_candy, max_candy_list)

print(max(max_candy_list))