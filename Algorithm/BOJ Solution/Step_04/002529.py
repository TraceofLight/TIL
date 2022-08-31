# 부등호

import sys


# 문제에서 주어진 부등호 조건을 만족하는지 체크하는 함수 선언
def check_condition(target_list, check_list):
    if len(target_list) == len(check_list) + 1:
        for idx in range(len(check_list)):
            if check_list[idx] == '>':
                if target_list[idx] < target_list[idx + 1]:
                    return False
            else:
                if target_list[idx] > target_list[idx + 1]:
                    return False
        return True


# 순열 공정을 진행하면서 조건을 만족한다면 첫 값을 return하는 함수 선언
def permutation(list, selection, first_selection):
    output = []
    if selection == 0:
        return [[]]
    for idx in range(len(list)):
        element = list[idx]
        for other in permutation(list[:idx] + list[idx + 1:], selection - 1, first_selection):
            check_this = [element] + other
            if len(check_this) != first_selection:
                output.append(check_this)
            else:
                if check_condition(check_this, condition):
                    return check_this
    return output


# 숫자 리스트 0 ~ 9 선언 (순열 공정 투입 시 0부터 사용)
# 따라서 최소값에 접근
number_list = list(range(10))
# 숫자 리스트 9 ~ 0 선언 (순열 공정 투입 시 9부터 사용)
# 따라서 최대값에 접근
number_list_rev = list(range(9, -1 , -1))

# 부등호 input
number = int(sys.stdin.readline())
condition = list(sys.stdin.readline().strip().split())[: number + 1]

# 자릿수는 부등호보다 1 크다
length_condition = len(condition) + 1
min_val = permutation(number_list, length_condition, length_condition)
max_val = permutation(number_list_rev, length_condition, length_condition)

# 최대값과 최소값 출력
print(''.join([str(element) for element in max_val]))
print(''.join([str(element) for element in min_val]))
