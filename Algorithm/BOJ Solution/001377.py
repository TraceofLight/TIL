# 버블 소트

import sys

# List input
number_amount = int(sys.stdin.readline())
number_list = []

# indexing
for counter in range(1, number_amount + 1):
    number_list.append([int(sys.stdin.readline()), counter])

# 정렬
number_list.sort()

# 기존 index 와 sort index 비교해서 역주행하는 것들 중 최대값으로 갱신
sub_max = 0
for idx in range(number_amount):
    if sub_max < number_list[idx][1] - (idx + 1):
        sub_max = number_list[idx][1] - (idx + 1)

# 마지막 체크 1회 더해서 출력
print(sub_max + 1)

# 버블 정렬의 단점
# 역방향으로 거슬러 올라가는 것은 1회 1칸씩만 가능

'''
# C++ 코드 변환

number_amount = int(sys.stdin.readline())
number_list = ['#']

for _ in range(number_amount):
    number_list.append(int(sys.stdin.readline()))

for end_bubble in range(1, number_amount):
    is_changed = False
    for idx in range(1, number_amount - end_bubble + 1):
        if number_list[idx] > number_list[idx + 1]:
            number_list[idx], number_list[idx + 1] \
                = number_list[idx + 1], number_list[idx]
            is_changed = True
    if not is_changed:
        print(end_bubble)
        break
'''
