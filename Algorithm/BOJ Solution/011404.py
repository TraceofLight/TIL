# 플로이드

import sys

# 도시 갯수, 노선 갯수 input()
city = int(sys.stdin.readline())
bus_number = int(sys.stdin.readline())

# 비용 리스트 INF로 초기화
cost_list = [[float('inf') for _ in range(city)] for _ in range(city)]

# 비용값 input
for _ in range(bus_number):
    start_city, end_city, cost = map(int, sys.stdin.readline().split())
    start_city -= 1
    end_city -= 1
    # 중복으로 들어오는 경우 그 중 최소값을 반영
    cost_list[start_city][end_city] = min(cost, cost_list[start_city][end_city])

# 자기 자신으로 이동하는 경우 0의 비용
for idx in range(city):
    cost_list[idx][idx] = 0

# 플로이드 - 워셜
for pass_point in range(city):
    for start_point in range(city):
        for end_point in range(city):
            # 중간 지점을 거칠 경우가 더 적은 비용을 지불할 경우 해당값으로 비용값을 갱신
            if cost_list[start_point][end_point] > cost_list[start_point][pass_point] + cost_list[pass_point][end_point]:
                cost_list[start_point][end_point] = cost_list[start_point][pass_point] + cost_list[pass_point][end_point]

# 도달할 수 없는 도시의 경우 INF가 유지
for start in range(city):
    for end in range(city):
        # 문제 조건에 따라 INF 전부 0으로 변환
        if cost_list[start][end] == float('inf'):
            cost_list[start][end] = 0

# 출력
for each_city in cost_list:
    print(*each_city)
