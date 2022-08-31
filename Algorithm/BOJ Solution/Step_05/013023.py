# ABCDE

import sys

# 사람의 수(node)와 관계의 수(line) input
node_number, line_number = map(int, sys.stdin.readline().split())

# 관계도 그래프 생성
graph = [set() for _ in range(node_number)]
for _ in range(line_number):
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node].add(end_node)
    graph[end_node].add(start_node)

# 결과값을 도중에 확인한 경우에 대한 Flag 생성
is_got_answer = False

# DFS
for start_node in range(node_number):
    # 이미 방문했다면 continue
    if not graph[start_node]:
        continue
    else:
        progress_que = []
        # 리스트에 방문 기록
        progress_que.append([start_node, 1, [start_node]])
        while progress_que:
            new_idx = progress_que.pop()
            # 방문 횟수가 5회인 경우 조건을 만족, Flag를 통해 반목문 escape
            if new_idx[1] == 5:
                is_got_answer = True
                break
            else:
                for element in graph[new_idx[0]]:
                    # 리스트에 기록한 방문을 통해 이미 방문한 노드 재방문 방지
                    if element not in new_idx[2]:
                        progress_que.append([element, new_idx[1] + 1, new_idx[2] + [element]])
        if is_got_answer:
            break

# 결과 출력
if is_got_answer:
    print(1)
else:
    print(0)