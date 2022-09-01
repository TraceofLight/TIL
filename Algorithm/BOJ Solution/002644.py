# 촌수계산

import sys

# 사람 수, 촌수 계산할 사람 input
people = int(sys.stdin.readline())
start_person, end_person = map(int, sys.stdin.readline().split())
start_person -= 1
end_person -= 1

# 그래프 생성
graph = [set() for _ in range(people)]
line_number = int(sys.stdin.readline())
for _ in range(line_number):
    first, second = map(int, sys.stdin.readline().split())
    first -= 1
    second -= 1
    graph[first].add(second)
    graph[second].add(first)

# 결과값 기본값 설정 (DFS 후 값을 찾지 못했다면 -1 출력)
calc_relation = -1

# DFS (진행한 횟수 리스트에 포함, 출발점에서 도착점에 도착했다면 진행횟수로 결과값 갱신)
progress_stack = []
progress_stack.append([start_person, 0])
is_visited = [False for _ in range(people)]
while progress_stack:
    now_person = progress_stack.pop()
    is_visited[now_person[0]] = True
    if is_visited[end_person]:
        calc_relation = now_person[1]
        break
    for element in graph[now_person[0]]:
        if not is_visited[element]:
            progress_stack.append([element, now_person[1] + 1])

# 결과 출력
print(calc_relation)