# 트리의 부모 찾기

import sys
from collections import defaultdict

# 노드 갯수 input
node_number = int(sys.stdin.readline())

# Line input
line_list = []
for _ in range(node_number - 1):
    line_list.append(list(map(int, sys.stdin.readline().split())))

# 그래프 생성
graph = [set() for _ in range(node_number)]
for line in line_list:
    start_node, end_node = line[0], line[1]
    start_node -= 1
    end_node -= 1
    graph[start_node].add(end_node)
    graph[end_node].add(start_node)

# 노드를 넣을 시 루트를 출력하는 딕셔너리 선언
val_dict = defaultdict(int)

# DFS 진행하면서 노드가 스택에 추가될 때 부모노드를 기록
progress_stack = []
progress_stack.append(0)
visited = [False for _ in range(node_number)]
while progress_stack:
    now_idx = progress_stack.pop()
    visited[now_idx] = True
    for element in graph[now_idx]:
        if not visited[element]:
            progress_stack.append(element)
            val_dict[element] = now_idx

# 2번 노드부터 딕셔너리에 넣어 결과값 출력
for number in range(1, node_number):
    print(val_dict[number] + 1)