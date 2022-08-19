import sys

node_number = int(sys.stdin.readline())
graph = [set() for _ in range(node_number)]

for start_node in range(node_number):
    line_list = list(map(int, sys.stdin.readline().split()))
    for end_node in range(node_number):
        if line_list[end_node] == 1:
            graph[start_node].add(end_node)

result = [[0 for _ in range(node_number)] for _ in range(node_number)]

for idx in range(node_number):
    progress_stack = []
    is_visited = [False for _ in range(node_number)]
    progress_stack.append(idx)
    while progress_stack:
        progress_idx = progress_stack.pop()
        for element in graph[progress_idx]:
            if not is_visited[element]:
                progress_stack.append(element)
                is_visited[element] = True
                result[idx][element] = 1

for row in result:
    print(*row)