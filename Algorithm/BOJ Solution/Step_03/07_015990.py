import sys
from collections import deque

testcase = int(sys.stdin.readline())
ans_list = deque([[1, 0 ,0], [0, 1, 0], [1, 1, 1]])
val_list = [1, 1, 3]
output = []


def plus_123(val):
    global val_list
    length = len(val_list)
    if val <= 3:
        return val_list[val - 1]
    else:
        for _ in range(length, val):
            ans_list.append([(ans_list[-1][1] + ans_list[-1][2]),
                            (ans_list[-2][0] + ans_list[-2][2]),
                            (ans_list[-3][0] + ans_list[-3][1])])
            val_list.append(sum(ans_list[-1]))
            ans_list.popleft()
        return val_list[val - 1] % 1000000009


for case in range(testcase):
    output.append(plus_123(int(sys.stdin.readline())))

print(*output, sep='\n')
