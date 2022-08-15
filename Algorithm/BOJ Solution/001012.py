import sys
from collections import deque

testcase = int(sys.stdin.readline())
output = []

for case in range(testcase):
    cabbage_list = []
    width, height, number = list(map(int, sys.stdin.readline().split()))
    for cabbage in range(number):
        cabbage_list.append(list(map(int, sys.stdin.readline().split())))

    # 그래프 생성
    visited = [False for _ in cabbage_list]
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    graph = [set() for _ in cabbage_list]
    for idx1 in range(number):
        for idx2 in range(number):
            if idx1 == idx2:
                continue
            for direction in directions:
                if ([cabbage_list[idx1][0] + direction[0], cabbage_list[idx1][1] + direction[1]] 
                    == [cabbage_list[idx2][0], cabbage_list[idx2][1]]):
                    graph[idx1].add(idx2)
                    graph[idx2].add(idx1)

    progress_que = deque([])
    result = 0
    # 그래프 내에서 BFS
    for idx in range(number):
        if visited[idx]:
            continue
        else:
            progress_que.append(idx)
            visited[idx] = True
            while progress_que:
                progress_idx = progress_que.popleft()
                for point in graph[progress_idx]:
                    if not visited[point]:
                        progress_que.append(point)
                        visited[point] = True
            result += 1
    output.append(result)

print(*output, sep='\n')