# 문자열 폭발

import sys
from collections import deque

string = deque(list(sys.stdin.readline().rstrip('\n')))
bomb = deque(list(sys.stdin.readline().rstrip('\n')))
progress_shelf = deque([])
total_length = len(string)
length = len(bomb)
shelf_length = 0
result = []

if total_length < length:
    print(''.join(string))

else:
    pass