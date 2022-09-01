# 창고 다각형

import sys
from collections import deque

# 기둥 숫자와 리스트 input
column_number = int(sys.stdin.readline())
column_list = []

# 기둥 위치, 높이 정보 input
for _ in range(column_number):
    column_list.append(list(map(int, sys.stdin.readline().split())))

# 순서 순으로 정렬
column_list.sort(key=lambda x:x[0])

# 각 기둥 위치 차이 및 길이 리스트 자료 정리
length_list = deque([])
for idx in range(column_number):
    length_list.append(column_list[idx][1])
# 길이 리스트를 뒤집은 리스트 추가
rev_length_list = deque(list(reversed(length_list)))
sub_list = deque([])
for idx in range(column_number - 1):
    sub_list.append(column_list[idx + 1][0] - column_list[idx][0])


# 중간의 고이는 구간을 배제하면서 최대 높이를 확인하는 함수 선언
def storage_column(list:deque):
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
    while result and result[-1] == last_big_number:
        result.pop()
    result.append(last_big_number)
    return result


# 최대 높이를 기준으로 좌우 리스트 함수를 통해 구현
list_front = deque(storage_column(length_list))
list_back = deque(list(reversed(storage_column(rev_length_list))))

# 최대 높이 변수 선언
big_number = list_front.pop()
list_back.popleft()

# 출력값 변수 선언
output = 0

# 좌우에서 1개의 길이를 계속 제거하면서 간격만큼 곱한 값을 출력값에 추가 
while list_front:
    output += list_front.popleft() * sub_list.popleft()
while list_back:
    output += list_back.pop() * sub_list.pop()

# 마지막에 리스트가 남았다면 최대 높이가 수평구간으로 존재한다는 것
if sub_list:
    for idx in range(len(sub_list)):
        output += sub_list.pop() * big_number
    output += big_number
# 아니라면 최대 높이가 수직 구간 딱 1줄 존재한다는 것
else:
    output += big_number

# 결과 출력
print(output)