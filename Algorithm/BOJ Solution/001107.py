import sys
from collections import deque

goal = int(sys.stdin.readline())
malfunction_amount = int(sys.stdin.readline())
button = set(range(10))
if malfunction_amount != 0:
    malfunction_list = set(map(int, sys.stdin.readline().split()))
else:
    malfunction_list = set()
available_button = button - malfunction_list


def bfs_remote(destination):
    global goal
    global available_button
    global malfunction_amount
    border = min(goal * 2 + 100, 600000)
    visited = [False for _ in range(600000)]
    result1 = 500000
    result2 = 500000
    # 숫자 처음부터 세팅할 경우
    if malfunction_amount != 10:
        print(malfunction_amount)
        progress_que = deque([])
        progress_que.append([0, 0, True])
        get_result = False
        while progress_que != deque([]):
            if get_result:
                break
            idx = progress_que.popleft()
            for number in available_button:
                if idx[0] * 10 + number < 2 * goal and idx[0] * 10 + number >= 0 and idx[2] == True:
                    if not visited[idx[0] * 10 + number]:
                        progress_que.append([idx[0] * 10 + number, idx[1] + 1, True])
                        visited[idx[0] * 10 + number] = True
                        if visited[destination]:
                            result1 = idx[1] + 1
                            get_result = True
                            break
            # 기본값 설정 보완
            if idx[0] == 0 and idx[1] == 0 and 0 in available_button:
                idx[1] += 1
                if visited[destination]:
                    result1 = idx[1]
                    get_result = True
                    break
            if idx[0] + 1 < border and idx[0] + 1 >= 0:
                if not visited[idx[0] + 1] :
                    progress_que.append([idx[0] + 1, idx[1] + 1, False])
                    visited[idx[0] + 1] = True
                    if visited[destination]:
                        result1 = idx[1] + 1
                        get_result = True
                        break
            if idx[0] - 1 < border and idx[0] - 1 >= 0:
                if not visited[idx[0] - 1]:
                    progress_que.append([idx[0] - 1, idx[1] + 1, False])
                    visited[idx[0] - 1] = True
                    if visited[destination]:
                        result1 = idx[1] + 1
                        get_result = True
                        break

    # 100부터 +, - 로만 변경
    visited_re = [False for _ in range(600000)]
    progress_que_100 = deque([])
    progress_que_100.append([100, 0])
    visited_re[100] = True
    if visited_re[destination] == True:
        return 0
    while progress_que_100 != deque([]):
        idx = progress_que_100.popleft()
        if idx[0] + 1 < border and idx[1] + 1 < result1 and idx[0] + 1 >= 0:
            if not visited_re[idx[0] + 1]:
                progress_que_100.append([idx[0] + 1, idx[1] + 1])
                visited_re[idx[0] + 1] = True
                if visited_re[destination]:
                    result2 = idx[1] + 1
                    break
        if idx[0] - 1 < border and idx[1] + 1 < result1 and idx[0] - 1 >= 0:
            if not visited_re[idx[0] - 1]:
                progress_que_100.append([idx[0] - 1, idx[1] + 1])
                visited_re[idx[0] - 1] = True
                if visited_re[destination]:
                    result2 = idx[1] + 1
                    break
    return min(result1, result2)


print(bfs_remote(goal))