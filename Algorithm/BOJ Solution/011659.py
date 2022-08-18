import sys

number, testcase = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0]
output = []

for idx in range(number):
    if idx == 0:
        sum_list.append(number_list[0])
    else:
        sum_list.append(sum_list[idx] + number_list[idx])

for case_each in range(testcase):
    start_num, end_num = map(int, sys.stdin.readline().split())
    output.append(sum_list[end_num] - sum_list[start_num - 1])

print(*output, sep='\n')
