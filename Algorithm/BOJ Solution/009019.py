import sys
from collections import deque
testcase = int(sys.stdin.readline())
output = []

for each_case in range(testcase):
    input_number, goal_number = map(int, sys.stdin.readline().split())
    progress_que = deque([])
    progress_que.append([input_number, '']) #숫자, 공정
    is_visited = [False for _ in range(10000)]
    while progress_que:
        progress_number = progress_que.popleft()
        number = progress_number[0] + 10000
        number_d = (number * 2) % 10000
        number_s = (number - 1) % 10000
        number_l = ((number % 1000) * 10 + ((number // 1000) - 10)) % 10000
        number_r = ((number % 10) * 1000 + ((number - 10000) // 10)) % 10000
        if not is_visited[number_d]:
            progress_que.append([number_d, progress_number[1] + 'D'])
            is_visited[number_d] = True
            if number_d == goal_number:
                output.append(progress_number[1] + 'D')
                break
        if not is_visited[number_s]:
            progress_que.append([number_s, progress_number[1] + 'S'])
            is_visited[number_s] = True
            if number_s == goal_number:
                output.append(progress_number[1] + 'S')
                break
        if not is_visited[number_l]:
            progress_que.append([number_l, progress_number[1] + 'L'])
            is_visited[number_l] = True
            if number_l == goal_number:
                output.append(progress_number[1] + 'L')
                break
        if not is_visited[number_r]:
            progress_que.append([number_r, progress_number[1] + 'R'])
            is_visited[number_r] = True
            if number_r == goal_number:
                output.append(progress_number[1] + 'R')
                break
    
print(*output, sep='\n')