# 트리 순회

import sys
from collections import deque

# 노드 갯수 input
node_number = int(sys.stdin.readline())

# 트리 데이터 input
tree = []
for _ in range(node_number):
    tree.append(list(sys.stdin.readline().split()))

# 트리 데이터 기반 그래프 생성
# 그래프 만들면서 ord 함수를 통해 ascii 숫자로 변환
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

# 순회 결과를 넣을 리스트 생성
result_list_preorder = []
result_list_inorder = []
result_list_postorder = []

# 전위순회 DFS로 진행, 시작점 0
progress_que = []
progress_que.append(0)
while progress_que:
    idx = progress_que.pop()
    if idx != '.':
        result_list_preorder.append(idx)
        for element in reversed(graph[idx]):
            progress_que.append(element)

# 중위 순회 및 후위 순회는 재귀 사용
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


# 각 결과 리스트들에 대해 string 변환
string_preorder = ''.join([chr(65 + number) for number in result_list_preorder])
string_inorder(graph, 0, result_list_inorder)
string_inorder_string = ''.join([chr(65 + number) for number in result_list_inorder])
string_postorder(graph, 0, result_list_postorder)
string_postorder_string = ''.join([chr(65 + number) for number in result_list_postorder])

# 결과 출력
print(string_preorder)
print(string_inorder_string)
print(string_postorder_string)
