import sys
from math import sqrt

testCase = int(sys.stdin.readline())
output = []
for i in range(testCase) :
    x1, y1, r1, x2, y2, r2 = list(map(int, sys.stdin.readline().split()))
    if r1 < r2:
        x2, y2, r2, x1, y1, r1 = x1, y1, r1, x2, y2, r2
    distance_sq = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    if distance_sq < r1:
        if x1 == x2 and y1 == y2 and r1 == r2:
            output.append(-1)
        elif x1 == x2 and y1 == y2 and r1 != r2:
            output.append(0)
        elif distance_sq + r2 < r1:
            output.append(0)
        elif distance_sq + r2 == r1:
            output.append(1)
        elif distance_sq + r2 > r1:
            output.append(2)
    elif distance_sq == r1:
        output.append(2)
    else:
        if r1 + r2 < distance_sq:
            output.append(0)
        elif r1 + r2 == distance_sq:
            output.append(1)
        elif r1 + r2 > distance_sq:
            output.append(2)

print(*output, sep='\n')