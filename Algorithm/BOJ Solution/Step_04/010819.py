import sys

number = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))


def permutation(number_list, select):
    result = []
    if select == 0:
        return [[]]
    for idx in range(len(number_list)):
        element = number_list[idx]
        for other in permutation(number_list[:idx] + number_list[idx + 1:], select - 1):
            result.append([element] + other)
    return result


def total_abs_difference(list):
    sum_number = 0
    for idx in range(len(list) - 1):
        sum_number += abs(list[idx] - list[idx + 1])
    return sum_number


output = []
for p_list in permutation(number_list, number):
    output.append(total_abs_difference(p_list))

print(max(output))