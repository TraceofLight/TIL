# 나이트의 이동

import sys
from collections import deque

# 케이스 횟수 input 및 출력 List 선언
testcase = int(sys.stdin.readline())
output = []
directions = [[2, 1], [1, 2], [1, -2], [2, -1], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]

for each_case in range(testcase):
    # 체스판의 너비, 시작점, 도착점 input
    length = int(sys.stdin.readline())
    start_point = list(map(int, sys.stdin.readline().rstrip().split()))
    end_point = list(map(int, sys.stdin.readline().rstrip().split()))
    # 시작점과 도착점이 같으면 0회 이동
    if start_point == end_point:
        output.append(0)
        continue
    else:
        # 방문 기록 리스트 선언
        is_visited = [[False for _ in range(length)] for _ in range(length)]
        # 결과 확인 후 반복문 탈출용 Flag 선언
        is_got_answer = False
        # BFS로 진행하면서 가장 먼저 나오는 값이 최소 횟수
        progress_que = deque([])
        progress_que.append([start_point, 0])
        is_visited[start_point[0]][start_point[1]] = True
        while progress_que:
            new_idx = progress_que.popleft()
            for direction in directions:
                if (new_idx[0][0] + direction[0] >= 0 and new_idx[0][0] + direction[0] < length and new_idx[0][1] + direction[1] >= 0 and new_idx[0][1] + direction[1] < length):
                    if not is_visited[new_idx[0][0] + direction[0]][new_idx[0][1] + direction[1]]:
                        is_visited[new_idx[0][0] + direction[0]][new_idx[0][1] + direction[1]] = True
                        if is_visited[end_point[0]][end_point[1]]:
                            output.append(new_idx[1] + 1)
                            is_got_answer = True
                            break
                        else:
                            progress_que.append([[new_idx[0][0] + direction[0], new_idx[0][1] + direction[1]], new_idx[1] + 1])
                if is_visited[end_point[0]][end_point[1]]:
                    output.append(new_idx[1])
                    break
            if is_got_answer:
                break

# 출력
for result in output:
    print(result)