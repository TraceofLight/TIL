import sys
from collections import deque

testcase = int(sys.stdin.readline())
output = []
cabbage_list = []
for case in range(testcase):
    width, height, amount = list(map(int, sys.stdin.readline().split()))
    for cabbage in range(amount):
        idx_x, idx_y = map(int, sys.stdin.readline().split())
        if idx_x < 0 or idx_x >= width or idx_y < 0 or idx_y >= height:
            continue
        else:
            cabbage_list.append([idx_x, idx_y])

    # 그래프 생성
    visited = [False for _ in cabbage_list]
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    graph = [[] for _ in cabbage_list]
    for idx1 in range(amount):
        for idx2 in range(amount):
            if idx1 == idx2:
                continue
            for direction in directions:
                if ([cabbage_list[idx1][0] + direction[0], cabbage_list[idx1][1] + direction[1]] 
                    == [cabbage_list[idx2][0], cabbage_list[idx2][1]]):
                    graph[idx1].append(idx2)
                    break

    progress_que = deque([])
    result = 0
    # 그래프 내에서 BFS
    for idx in range(amount):
        if visited[idx]:
            continue
        else:
            progress_que.append(idx)
            visited[idx] = True
            while progress_que:
                progress_idx = progress_que.pop()
                for point in graph[progress_idx]:
                    if not visited[point]:
                        progress_que.append(point)
                        visited[point] = True
            result += 1
    output.append(result)

print(*output, sep='\n')

'''
    # 그래프 내에서 DFS
    for idx in range(amount):
        if visited[idx]:
            continue
        else:
            progress_que.append(idx)
            while progress_que != deque([]):
                progress_idx = progress_que.popleft()
                visited[progress_idx] = True
                for cabbage_point in graph[progress_idx]:
                    if not visited[cabbage_point]:
                        progress_que.append(cabbage_point)
            result += 1
'''