import sys
from collections import deque

node_number, line_number, init_node = map(int, sys.stdin.readline().split())

graph = [set() for _ in range(node_number)]
node_set = set()

def dfs(node_num, graph_list, start):
    visited = [False for _ in range(node_num)]
    result = []
    progress_que = deque([])

    progress_que.append(start - 1)
    while progress_que != deque([]):
        progress_idx = progress_que.pop()
        if not visited[progress_idx]:
            visited[progress_idx] = True
            result.append(progress_idx + 1)
            for node in sorted(list(graph_list[progress_idx]), key=lambda x:-x):
                    progress_que.append(node)
    
    return result

def bfs(node_num, graph_list, start):
    visited = [False for _ in range(node_num)]
    result = []
    progress_que = deque([])

    progress_que.append(start - 1)
    while progress_que != deque([]):
        progress_idx = progress_que.popleft()
        if not visited[progress_idx]:
            visited[progress_idx] = True
            result.append(progress_idx + 1)
            for node in sorted(list(graph_list[progress_idx])):
                    progress_que.append(node)
    
    return result

print(*dfs(node_number, graph, init_node))
print(*bfs(node_number, graph, init_node))