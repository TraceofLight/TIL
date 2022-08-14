import sys 

testcase = int(sys.stdin.readline())
output = []
sum_list = [1, 2, 4]

def sum_123(val):
    global sum_list
    if len(sum_list) >= val:
        return sum_list[val - 1]
    else:
        for idx in range(len(sum_list), val):
            sum_list.append(sum_123(idx) + sum_123(idx - 1) + sum_123(idx - 2))
        return sum_list[val - 1]


for case in range(testcase):
    output.append(sum_123(int(sys.stdin.readline())))

print(*output, sep='\n')