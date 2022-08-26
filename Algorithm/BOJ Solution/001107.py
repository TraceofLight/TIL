import sys
from collections import deque

destination = int(sys.stdin.readline())
malfunction_number = int(sys.stdin.readline())
if malfunction_number:
    malfunction_list = list(map(int, sys.stdin.readline().split()))
    button = [number for number in range(10) if number not in malfunction_list]
else:
    button = [number for number in range(10)]

option1 = abs(destination - 100)

is_visited = [False for _ in range(1000001)]
progress_que = deque([])
if button:
    for channel_number in button:
        progress_que.append([channel_number, 1, True])
else:
    progress_que.append([100, 1, False])
while progress_que:
    idx = progress_que.popleft()
    is_visited[idx[0]] = True
    if is_visited[destination]:
        option2 = idx[1]
        break
    for append_number in button:
        if idx[0] * 10 + append_number <= 1000000 and idx[0] * 10 + append_number >= 0:
            if not is_visited[idx[0] * 10 + append_number] and idx[2]:
                progress_que.append([idx[0] * 10 + append_number, idx[1] + 1, True])
    if idx[0] + 1 <= 1000000 and idx[0] + 1 >= 0 :
        if not is_visited[idx[0] + 1]:
            progress_que.append([idx[0] + 1, idx[1] + 1, False])
    if idx[0] - 1 >= 0 and idx[0] - 1 <= 1000000:
        if not is_visited[idx[0] - 1]:
            progress_que.append([idx[0] - 1, idx[1] + 1, False])

print(min(option1, option2))