import sys
from collections import deque

testcase = int(sys.stdin.readline())
output = []
cabbage_list = []
for case in range(testcase):
    width, height, amount = list(map(int, sys.stdin.readline().split()))
    counter = 0
    for cabbage in range(amount):
        idx_x, idx_y = list(map(int, sys.stdin.readline().split()))
        cabbage_list.append([idx_x, idx_y, counter])
        counter += 1

    # 그래프 생성
    visited = [False for _ in cabbage_list]
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    graph = [[] for _ in cabbage_list]
    for idx1 in range(amount):
        for idx2 in range(amount):
            for direction in directions:
                if not (cabbage_list[idx1][0] + direction[0] < 0 or cabbage_list[idx1][0] + direction[0] >= width or 
                        cabbage_list[idx1][1] + direction[1] < 0 or cabbage_list[idx1][1] + direction[1] >= height):
                    if [cabbage_list[idx1][0] + direction[0], cabbage_list[idx1][1] + direction[1]] == [cabbage_list[idx2][0], cabbage_list[idx2][1]]:
                        graph[idx1].append(cabbage_list[idx2])
    
    progress_que = deque([])
    result = 0
    # 그래프 내에서 BFS
    for idx in range(amount):
        if visited[idx]:
            continue
        else: 
            progress_que.append(cabbage_list[idx])
            while progress_que != deque([]):
                index_dfs = progress_que[-1][2]
                visited[index_dfs] = True
                for cabbage_point in graph[index_dfs]:
                    if not visited[cabbage_point[2]]:
                        visited[cabbage_point[2]] == True
                        progress_que.append(cabbage_list[cabbage_point[2]])
                progress_que.popleft()
            result += 1
    output.append(result)

print(*output, sep='\n')
