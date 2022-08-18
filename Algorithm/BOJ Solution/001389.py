import sys
from collections import deque

node_number, line_number = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node_number)]
bacon_number = [0 for _ in range(node_number)]

for _ in range(line_number):
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node - 1].append([end_node - 1, 0])
    graph[end_node - 1].append([start_node - 1, 0])

for idx in range(node_number):
    is_visited = [False for _ in range(node_number)]
    progress_stack = deque([])
    progress_stack.append([idx, 0])
    is_visited[idx] = True
    sum_bacon = 0
    while progress_stack:
        progress_idx = progress_stack.popleft()
        for element in graph[progress_idx[0]]:
            if not is_visited[element[0]]:
                element[1] = progress_idx[1] + 1
                is_visited[element[0]] = True
                sum_bacon += element[1]
                progress_stack.append(element)
    bacon_number[idx] = sum_bacon

print(bacon_number.index(min(bacon_number)) + 1)
