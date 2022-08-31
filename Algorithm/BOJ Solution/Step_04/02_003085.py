# 사탕게임

import sys

# 길이 input
length = int(sys.stdin.readline())

# 2차원 리스트 input
matrix_candy = []
for _ in range(length):
    matrix_candy.append(list(sys.stdin.readline().strip()))

# row에 대해서 최대 길이를 확인하는 함수 선언
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

# matrix 전체에 대해서 최대 최대 길이 확인 함수를 사용
# 전체 행과 열에 대해 최대값을 반환하는 함수 선언
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

# 행렬을 뒤집고 다시 되돌리는 함수 선언
def change_n_check(spot1_a, spot1_b, spot2_a, spot2_b, matrix_list, result_list):
    matrix_list[spot1_a][spot1_b], matrix_list[spot2_a][spot2_b] = matrix_list[spot2_a][spot2_b], matrix_list[spot1_a][spot1_b]
    result_list.append(max_candy(matrix_list))
    matrix_list[spot1_a][spot1_b], matrix_list[spot2_a][spot2_b] = matrix_list[spot2_a][spot2_b], matrix_list[spot1_a][spot1_b]

# 행렬을 뒤집었을 때의 모든 최대값을 저장하는 리스트 선언
max_candy_list = []

for y_idx in range(length):
    for x_idx in range(length):
        if y_idx == length - 1:
            # x, y가 전부 마지막인 경우 뒤집을 가로, 세로값이 없으므로 continue
            if x_idx == length - 1:
                continue
            # x, y 가 하나만 마지막 index인 경우 가능한 가로, 세로에 대해 한 번씩 뒤집기
            else:
                change_n_check(y_idx, x_idx, y_idx, x_idx + 1, matrix_candy, max_candy_list)
        else:
            if x_idx == length - 1:
                change_n_check(y_idx, x_idx, y_idx + 1, x_idx, matrix_candy, max_candy_list)
            else:
                # 마지막 index가 아닌 값들은 가로, 세로 총 2번 뒤집기가 가능
                change_n_check(y_idx, x_idx, y_idx, x_idx + 1, matrix_candy, max_candy_list)
                change_n_check(y_idx, x_idx, y_idx + 1, x_idx, matrix_candy, max_candy_list)

# 최대값들 중 가장 큰 결과값을 출력
print(max(max_candy_list))
