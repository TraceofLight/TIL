# 정수 삼각형

import sys
from collections import deque

line_number = int(sys.stdin.readline())
triangle_stack = deque([])

counter = 0
for y_idx in range(line_number):
    triangle_stack.append(list(map(int, sys.stdin.readline().split())))

number = 0
while triangle_stack:
    number += 1
    now_list = triangle_stack.popleft()
    counter = 2
    while now_list:
        pass
