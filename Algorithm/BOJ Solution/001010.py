import sys

testcase = int(sys.stdin.readline())
factorial_list = [1]
output = []


def factorial(val):
    global factorial_list
    length = len(factorial_list)
    if val <= length - 1:
        return factorial_list[val]
    else:
        for idx in range(length, val + 1):
            factorial_list.append(factorial_list[idx - 1] * idx)
        return factorial_list[val]


for case in range(testcase):
    n, m = list(map(int, sys.stdin.readline().split()))
    result = (factorial(m) // factorial(m - n)) // factorial(n)
    output.append(result)

print(*output, sep='\n')
