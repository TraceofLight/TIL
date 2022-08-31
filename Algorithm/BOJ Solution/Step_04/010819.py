# 차이를 최대로

import sys

# 숫자의 갯수와 List input
number = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))


# 순열 함수 선언
def permutation(number_list, select):
    result = []
    if select == 0:
        return [[]]
    for idx in range(len(number_list)):
        element = number_list[idx]
        for other in permutation(number_list[:idx] + number_list[idx + 1:], select - 1):
            result.append([element] + other)
    return result


# 전체 리스트에 대해서 차이값 연산하는 함수 선언
def total_abs_difference(list):
    sum_number = 0
    for idx in range(len(list) - 1):
        sum_number += abs(list[idx] - list[idx + 1])
    return sum_number


# 함수들을 조합하여 모든 배열에 대해 차이값 연산
output = []
for p_list in permutation(number_list, number):
    output.append(total_abs_difference(p_list))

# 최대값을 출력
print(max(output))
