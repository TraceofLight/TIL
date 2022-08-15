import sys
from collections import deque

nodes, lines, start_point = list(map(int, sys.stdin.readline().split()))
line_list = []
line_list_raw = [set() for _ in range(nodes)]
visited = [False for _ in range(nodes)]

for _ in range(lines):
    start_node, end_node = map(int, sys.stdin.readline().split())
    line_list_raw[start_node - 1].add(end_node)
    line_list_raw[end_node - 1].add(start_node)

line_list = [sorted(list(element)) for element in line_list_raw]

progress_que = deque([])
result = []

progress_que.append(start_point)
visited[start_point - 1] = True
result.append(start_point)
while progress_que != deque([]):
    progress_idx = progress_que.popleft() - 1
    for element in line_list[progress_idx]:
        if not visited[element - 1]:
            progress_que.append(element)
            visited[element - 1] = True
            result.append(element)

visit_data_raw = list(enumerate(result))
visit_dict = {data[1]: data[0] for data in visit_data_raw}

for node in range(1, nodes + 1):
    if visit_dict.get(node) == None:
        print(0)
    else:
        print(visit_dict.get(node) + 1)

'''
loop_list = []
loop_list.append(start_point)
for idx in range(1, nodes + 1):
    if idx == start_point:
        continue
    loop_list.append(idx)

for idx in loop_list:
    if not idx in visited:
        progress_que.append(idx)
        visited.append(idx)
        while progress_que != deque([]):
            progress_idx = progress_que.popleft() - 1
            for element in node_list[progress_idx]:
                if element not in visited:
                    progress_que.append(element)
                    visited.append(element)
'''
