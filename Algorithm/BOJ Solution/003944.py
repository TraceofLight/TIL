import sys
from collections import deque

testCase = int(sys.stdin.readline().strip())
output = []

for i in range(testCase) :
    b, d = sys.stdin.readline().split()
    number_list = deque([int(i) for i in d])
    b = int(b)
    devide_number = 0
    length = len(number_list)
    while length > 0 :
        a = number_list.popleft()
        if a + devide_number >= (b - 1)  :
            devide_number = ((devide_number + a) % (b - 1)) * b
        elif a + devide_number < (b - 1)  :
            devide_number = (devide_number + a) * b
        length -= 1
        if length == 0 :
            devide_number = devide_number % (b - 1)
    output.append(devide_number)
print(*output, sep = '\n')


'''
import sys

testCase = int(sys.stdin.readline().strip())
output = []

for i in range(testCase) :
    b, d = sys.stdin.readline().split()
    b = int(b)
    number_list = list(d)
    length = len(number_list)
    devide_number = 0
    for idx, my in enumerate(number_list):
        devide_number += int(my)*(b**(length-idx-1)) % (b-1)
    output.append(devide_number % (b-1))

print(*output, sep = '\n')
'''