import sys
from collections import deque

testcase = int(sys.stdin.readline())
output = []
directions = [[2, 1], [1, 2], [1, -2], [2, -1], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]

for each_case in range(testcase):
    length = int(sys.stdin.readline())
    start_point = list(map(int, sys.stdin.readline().rstrip().split()))
    end_point = list(map(int, sys.stdin.readline().rstrip().split()))
    if start_point == end_point:
        output.append(0)
        continue
    else:
        is_visited = [[False for _ in range(length)] for _ in range(length)]
        is_got_answer = False
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

for result in output:
    print(result)