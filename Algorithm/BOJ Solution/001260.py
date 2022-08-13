'''
from collections import deque

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
  
print(BFS_with_adj_list(graph_list, root_node))
'''

import sys
from collections import deque

NodeNumber, LineNumber, StartNode = list(map(int,sys.stdin.readline().split()))

NodeList = [set() for i in range(NodeNumber)]

for number in range(LineNumber) :
    idx, destination = list(map(int, sys.stdin.readline().split()))
    NodeList[idx].add(destination)

visited = []
def BFS(NodeList, node, NodeNumber) :
    global visited
    queue = deque([node])

    while queue :
        if len(visited) == NodeNumber :
            return visited
        number = queue.popleft()
        if number not in visited :
            visited.append(number)
            if NodeList[number - 1] != set() :
                queue += NodeList[number - 1] - set(visited)
    return BFS(NodeList, visited, NodeNumber)

print(BFS(NodeList, StartNode, NodeNumber))