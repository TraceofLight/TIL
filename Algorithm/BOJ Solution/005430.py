import sys
from collections import deque

testcase = int(sys.stdin.readline().rstrip('\n'))
output = []

for each_case in range(testcase):
    command_list = list(sys.stdin.readline().rstrip('\n'))
    length = int(sys.stdin.readline().rstrip('\n'))
    string_raw = sys.stdin.readline().strip('\n')
    if string_raw == '[]':
        number_list = []
    else:
        string = string_raw.lstrip('[').rstrip(']')
        number_list = list(map(int, string.split(',')))
    number_que = deque(number_list)
    counter = 0
    is_reversed = counter % 2
    is_find_answer = False
    for command in command_list:
        if command == 'R':
            counter += 1
            is_reversed = counter % 2
        if command == 'D':
            is_reversed = counter % 2
            if length == 0:
                output.append('error')
                is_find_answer = True
                break
            else:
                if not is_reversed:
                    number_que.popleft()
                    length -= 1
                else:
                    number_que.pop()
                    length -= 1
    if is_find_answer:
        continue
    else:
        is_reversed = counter % 2
        result = '['
        if not is_reversed:
            while number_que:
                result = result + str(number_que.popleft())
                if number_que:
                    result = result + ','
            result = result + ']'
            output.append(result)
        else:
            while number_que:
                result = result + str(number_que.pop())
                if number_que:
                    result = result + ','
            result = result + ']'
            output.append(result)

print(*output, sep='\n')