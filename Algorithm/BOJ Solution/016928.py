import sys
from collections import deque

ladder, snake = map(int, sys.stdin.readline().split())
graph = [set() for _ in range(100)]
is_visited = [False for _ in range(100)]

for idx in range(100):
    for dice_number in range(1, 7):
        if idx + dice_number <= 99:
            graph[idx].add(idx + dice_number)

ladder_n_snake = []

for _ in range(ladder):
    start_node, end_node = map(int, sys.stdin.readline().split())
    start_node -= 1
    end_node -= 1
    graph[start_node].clear()
    graph[start_node].add(end_node)
    ladder_n_snake.append(start_node)

for _ in range(snake):
    start_node, end_node = map(int, sys.stdin.readline().split())
    start_node -= 1
    end_node -= 1
    graph[start_node].clear()
    graph[start_node].add(end_node)
    ladder_n_snake.append(start_node)

start_point = 0
progress_que = deque([])
progress_que.append([start_point, 0])
result = float('inf')

while progress_que:
    idx = progress_que.popleft()
    if idx[0] == 99:
        result = idx[1]
        break
    else:
        if not is_visited[idx[0]]:
            is_visited[idx[0]] = True
            for element in graph[idx[0]]:
                if not is_visited[element]:
                    if idx[0] in ladder_n_snake:
                        progress_que.appendleft([element, idx[1]])
                    else:
                        progress_que.append([element, idx[1] + 1])

print(result)