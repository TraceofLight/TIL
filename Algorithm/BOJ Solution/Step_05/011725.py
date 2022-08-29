import sys
from collections import defaultdict

node_number = int(sys.stdin.readline())

line_list = []
for _ in range(node_number - 1):
    line_list.append(list(map(int, sys.stdin.readline().split())))

graph = [set() for _ in range(node_number)]

for line in line_list:
    start_node, end_node = line[0], line[1]
    start_node -= 1
    end_node -= 1
    graph[start_node].add(end_node)
    graph[end_node].add(start_node)

val_dict = defaultdict(int)

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

for number in range(1, node_number):
    print(val_dict[number] + 1)