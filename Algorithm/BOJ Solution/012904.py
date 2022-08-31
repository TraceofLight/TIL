# A와 B

import sys

# string input
start_string = list(sys.stdin.readline().rstrip('\n'))
goal_string = list(sys.stdin.readline().rstrip('\n'))

# 각 string 길이 선언
length = len(start_string)
now_length = len(goal_string)

# 도착 string에서부터 역연산
# 길이가 초기값보다 작아지지 않았을 경우만 지속
while now_length >= length:
    # 같아졌을 경우 두 string이 같은지 체크해서 결과 출력
    if length == now_length:
        if goal_string == start_string:
            print(1)
            break
        else:
            print(0)
            break
    # 끝자리가 A 일 경우 역순으로 진행
    if goal_string[-1] == 'A':
        goal_string.pop()
        now_length -= 1
    # 끝자리가 B 일 경우 역순으로 진행
    elif goal_string[-1] == 'B':
        goal_string.pop()
        goal_string.reverse()
        now_length -= 1
