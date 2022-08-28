import sys

node_number, line_number = map(int, sys.stdin.readline().split())
graph = [set() for _ in range(node_number)]
for _ in range(line_number):
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node].add(end_node)
    graph[end_node].add(start_node)

is_got_answer = False

for start_node in range(node_number):
    if not graph[start_node]:
        continue
    else:
        progress_que = []
        progress_que.append([start_node, 1, [start_node]])
        while progress_que:
            new_idx = progress_que.pop()
            if new_idx[1] == 5:
                is_got_answer = True
                break
            else:
                for element in graph[new_idx[0]]:
                    if element not in new_idx[2]:
                        progress_que.append([element, new_idx[1] + 1, new_idx[2] + [element]])
        if is_got_answer:
            break

if is_got_answer:
    print(1)
else:
    print(0)