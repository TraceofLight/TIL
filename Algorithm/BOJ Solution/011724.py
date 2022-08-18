import sys

node_number, line_number = map(int, sys.stdin.readline().split())

is_visited = [False for _ in range(node_number)]
graph = [set() for _ in range(node_number)]

for _ in range(line_number):
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node - 1].add(end_node - 1)
    graph[end_node - 1].add(start_node - 1)

result = 0

for idx in range(node_number):
    if is_visited[idx]:
        continue
    else:
        progess_stack = []
        progess_stack.append(idx)
        is_visited[idx] = True
        while progess_stack != []:
            target_idx = progess_stack.pop()
            for element in graph[target_idx]:
                if not is_visited[element]:
                    progess_stack.append(element)
                    is_visited[element] = True
        result += 1

print(result)
