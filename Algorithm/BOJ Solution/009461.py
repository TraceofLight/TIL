import sys

testcase = int(sys.stdin.readline())
output = []

for case_each in range(testcase):
    padovan = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    target = int(sys.stdin.readline())
    if target <= 10:
        output.append(padovan[target - 1])
    else:
        for idx in range(10, target):
            padovan.append(padovan[idx - 1] + padovan[idx - 5])
        output.append(padovan[target - 1])

print(*output, sep='\n')