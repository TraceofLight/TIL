# DFS와 BFS

import sys
from collections import deque

# 노드, 라인의 갯수 및 시작점 input
node_number, line_number, init_node = map(int, sys.stdin.readline().split())

# 그래프 생성
graph = [set() for _ in range(node_number)]
for _ in range(line_number):
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node - 1].add(end_node - 1)
    graph[end_node - 1].add(start_node - 1)


# DFS와 BFS 함수 선언
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


# 결과 출력
print(*dfs(node_number, graph, init_node))
print(*bfs(node_number, graph, init_node))