import sys
from collections import deque

node_number = int(sys.stdin.readline())

tree = []
for _ in range(node_number):
    tree.append(list(sys.stdin.readline().split()))

graph = [deque([]) for _ in range(node_number)]

for tree_part in tree:
    tree_node, left_branch, right_branch = tree_part[0], tree_part[1], tree_part[2]
    if right_branch != '.':
        graph[ord(tree_node) - 65].appendleft(ord(right_branch) - 65)
    else:
        graph[ord(tree_node) - 65].appendleft('.')
    if left_branch != '.':
        graph[ord(tree_node) - 65].appendleft(ord(left_branch) - 65)
    else:
        graph[ord(tree_node) - 65].appendleft('.')

result_list_preorder = []
result_list_inorder = []
result_list_postorder = []

progress_que = []
progress_que.append(0)
while progress_que:
    idx = progress_que.pop()
    if idx != '.':
        result_list_preorder.append(idx)
        for element in reversed(graph[idx]):
            progress_que.append(element)

def string_inorder(graph, start_number, list:list):
    if graph[start_number][0] != '.':
        string_inorder(graph, graph[start_number][0], list)
    list.append(start_number)
    if graph[start_number][1] != '.':
        string_inorder(graph, graph[start_number][1], list)

def string_postorder(graph, start_number, list:list):
    if graph[start_number][0] != '.':
        string_postorder(graph, graph[start_number][0], list)
    if graph[start_number][1] != '.':
        string_postorder(graph, graph[start_number][1], list)
    list.append(start_number)

string_preorder = ''.join([chr(65 + number) for number in result_list_preorder])
string_inorder(graph, 0, result_list_inorder)
string_inorder_string = ''.join([chr(65 + number) for number in result_list_inorder])
string_postorder(graph, 0, result_list_postorder)
string_postorder_string = ''.join([chr(65 + number) for number in result_list_postorder])
print(string_preorder)
print(string_inorder_string)
print(string_postorder_string)
