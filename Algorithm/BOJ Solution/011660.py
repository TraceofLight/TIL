import sys

length, testcase = map(int, sys.stdin.readline().split())

matrix = []
sum_row = []

for _ in range(length):
    row_list = list(map(int, sys.stdin.readline().split()))
    counter = 0
    row = 0
    sum_row.append([0])
    while counter != length:
        row += row_list[counter]
        sum_row[-1].append(row)
        counter += 1
    matrix.append(row_list)

output = []

for each_case in range(testcase):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    y2 -= 1
    sum_result = 0
    for idx in range(y2 - y1 + 1):
        sum_result += sum_row[y1 + idx][x2] - sum_row[y1 + idx][x1]
    output.append(sum_result)

for result in output:
    print(result)