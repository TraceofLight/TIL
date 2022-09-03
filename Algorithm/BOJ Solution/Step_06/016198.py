# 에너지 모으기

import sys

# 구슬 갯수 및 리스트 input
marble_number = int(sys.stdin.readline())
marble_list = list(map(int, sys.stdin.readline().split()))

# 최대값 변수 선언
max_energy = 0

# DFS를 통해 전체 가짓수 조회
progress_stack = []
# 각 구슬에 대해 초기값 추가
for idx in range(1, marble_number - 1):
    progress_stack.append( # 제거된 구슬 리스트, 에너지 총합, 카운팅
        [[idx], marble_list[idx - 1] * marble_list[idx + 1], 1]
    )

while progress_stack:
    now_marble = progress_stack.pop()
    # 종료 조건 : 맨 앞과 맨 뒤를 제외하고 모든 구슬이 제거
    if now_marble[2] == marble_number - 2:
        # 기존 최대값보다 크다면 갱신
        if now_marble[1] > max_energy:
            max_energy = now_marble[1]
    else:
        for idx in range(1, marble_number - 1):
            # 제거되지 않은 구슬에 대해서 이어서 진행
            if idx not in now_marble[0]:
                # 좌우 구슬의 무게 조사
                # 이미 제거된 구슬이라면 좌우 구슬 index에서 배제
                counter_plus = 1
                while idx + counter_plus in now_marble[0]:
                    counter_plus += 1
                counter_minus = 1
                while idx - counter_minus in now_marble[0]:
                    counter_minus += 1
                # 제거 구슬에 현 index를 추가하고 좌우 구슬 무게의 곱을 에너지에 합산, 카운팅 1 추가
                progress_stack.append(
                    [now_marble[0] + [idx],
                    now_marble[1] + marble_list[idx + counter_plus] * marble_list[idx - counter_minus],
                    now_marble[2] + 1]
                )

# 최대값 출력
print(max_energy)
