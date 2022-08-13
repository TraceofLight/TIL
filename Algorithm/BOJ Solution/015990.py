import sys

testcase = int(sys.stdin.readline())
#ans_list = [0, [1, 0 ,0], [0, 1, 0], [1, 1, 1]]
ans_list = [1, 1, 1, 3, 3, 3, 9]
output = []


def plus_123(val):
    global ans_list
    for _ in range(4, val + 1):
        '''
        ans_list.append([(ans_list[-1][1] + ans_list[-1][2]),
                        (ans_list[-2][0] + ans_list[-2][2]),
                        (ans_list[-3][0] + ans_list[-3][1])])
        '''

        ans_list.append((ans_list[-1] - ans_list[-2]) +
                        (ans_list[-2] - ans_list[-4]) +
                        (ans_list[-3] - ans_list[-6]))

plus_123(100000)

for case in range(testcase):
    output.append(ans_list[(int(sys.stdin.readline()))] % 1000000009)

print(*output, sep='\n')
