import sys
from collections import deque

start, end = map(int, sys.stdin.readline().split())

# BFS

if end <= start:
    print(start - end)
else:
    visited = [False for _ in range(0, 200001)]
    process_que = deque([])
    process_que.append([start, 0])
    while True:
        idx = process_que.popleft()
        visited[idx[0]] = True
        if 2 * idx[0] >= 0 and 2 * idx[0] <= 200000:
            if not visited[2 * idx[0]]:
                process_que.append([2 * idx[0], idx[1] + 1])
                visited[2 * idx[0]] = True
                if visited[end] == True:
                    print(idx[1] + 1)
                    break
        if idx[0] + 1 >= 0 and idx[0] + 1 <= 200000:
            if not visited[idx[0] + 1]:
                process_que.append([idx[0] + 1, idx[1] + 1])
                visited[idx[0] + 1] = True
                if visited[end] == True:
                    print(idx[1] + 1)
                    break
        if idx[0] - 1 >= 0 and idx[0] - 1 <= 200000:
            if not visited[idx[0] - 1]:
                process_que.append([idx[0] - 1, idx[1] + 1])
                visited[idx[0] - 1] = True
                if visited[end] == True:
                    print(idx[1] + 1)
                    break