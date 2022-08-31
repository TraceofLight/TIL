# 팰린드롬 만들기

import sys
from collections import deque
from copy import deepcopy

# 문자열 input
string = deque(list(sys.stdin.readline().rstrip('\n')))
# 길이 변수 선언
length = len(string)


# 펠린드롬 체크 함수 선언
def check_pelindrome(use_string_origin, leng):
    string = deepcopy(use_string_origin)
    for idx in range(leng // 2):
        last_letter = string.pop()
        if string[idx] != last_letter:
            return False
    return True


# pop 카운팅 변수 선언
pop_counter = 0
# 문자열 맨 앞에서부터 제거하면서 남은 문자열이 펠린드롬인지 체크
while True:
    if check_pelindrome(string, length):
        # 펠린드롬이라면 제거한 문자열 전후로 붙여서 펠린드롬화
        print(pop_counter * 2 + length)
        break
    else:
        # 펠린드롬이 아니라면 계속 문자열 제거
        pop_counter += 1
        length -= 1
        string.popleft()
