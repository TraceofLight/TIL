# 창고 다각형

import sys
from collections import deque

column_number = int(sys.stdin.readline())
column_list = []

for _ in range(column_number):
    column_list.append(list(map(int, sys.stdin.readline().split())))

column_list.sort(key=lambda x:x[0])

length_list = deque([])
for idx in range(column_number):
    length_list.append(column_list[idx][1])
rev_length_list = deque(list(reversed(length_list)))
sub_list = deque([])
for idx in range(column_number - 1):
    sub_list.append(column_list[idx + 1][0] - column_list[idx][0])
sub_list.append(1)

def check_max_list(list:deque):
    progress_list = list
    result = []
    last_big_number = 0
    while progress_list:
        if not result:
            last_big_number = progress_list.popleft()
            result.append(last_big_number)
        else:
            now_number = progress_list.popleft()
            if last_big_number < now_number:
                last_big_number = now_number
                result.append(now_number)
            else:
                result.append(last_big_number)
    while result[-1] == last_big_number:
        result.pop()
    result.append(last_big_number)
    return result

list_front = deque(check_max_list(length_list))
list_back = list(reversed(check_max_list(rev_length_list)))

big_number = list_front.pop()
list_back.pop(0)
output = 0

while list_front:
    output += list_front.popleft() * sub_list.popleft()
while list_back:
    output += list_back.pop() * sub_list.pop()
while sub_list:
    output += sub_list.pop() * big_number

print(output)