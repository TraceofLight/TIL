import sys
from collections import deque

nodes, lines, start_point = list(map(int, sys.stdin.readline().split()))
line_list = []
node_list = [set() for _ in range(nodes)]
visited = []

for idx in range(lines):
    line_list.append(list(map(int, sys.stdin.readline().split())))

for line in line_list:
    node_list[line[0] - 1].add(line[1])


def bfs_funtion(first_node, node_list1):
    global visited
    process_que = deque([])
    print(process_que)
    process_que.append(first_node)
    visited.append(first_node)
    while set(visited) == set(node_list) :
        if process_que != deque([]):
            node_number = process_que.popleft()
            process_list = sorted(list(node_list1[node_number - 1]))
            for element in process_list:
                if element in visited:
                    continue
                else:
                    process_que.append(element)
                    visited.append(element)
    return visited


bfs_funtion(start_point, node_list)

counter = 1
result_list = []
for number in visited :
    result_list.append([number, counter])
    counter += 1
result_dict = dict(result_list)

print(visited)
for idx in range(nodes):
    output = result_dict.get(idx + 1)
    if output == None:
        print(0)
    else:
        print(output)