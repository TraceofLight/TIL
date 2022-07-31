import sys

output = []

for i in range(3) :
    testCase = int(sys.stdin.readline())
    sum_number = 0
    for j in range(testCase) :
        sum_number += int(sys.stdin.readline())
    if sum_number > 0 :
        output.append('+')
    elif sum_number < 0 :
        output.append('-')
    else :
        output.append(0)

print(*output, sep = '\n')