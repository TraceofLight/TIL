from collections import deque
import sys

testCase = int(input())
output = []

for i in range(testCase) :
    amount, target = list(map(int,sys.stdin.readline().split()))
    print_list_raw = list(map(int,sys.stdin.readline().split()))
    print_list = deque(enumerate(print_list_raw))
    priority_list = sorted(print_list_raw)
    length = amount
    counter = 0

    while True :
        print_now = print_list.popleft() 
        if print_now[1] == priority_list[-1] :
            priority_list.pop()
            counter += 1
            length -= 1
            if print_now[0] == target :
                output.append(counter)
        else :
            print_list.append(print_now)
        if length == 0 :
            break

for result in output :
    print(result)