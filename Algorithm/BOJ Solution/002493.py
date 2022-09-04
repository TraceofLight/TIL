# 탑

import sys
from collections import deque

# 타워 수와 리스트 input
tower_number = int(sys.stdin.readline())
tower_list = deque(list(map(int, sys.stdin.readline().rstrip('\n').split())))

# 공정 처리 stack과 결과 리스트 선언
progress = []
result = []

# 인덱스 변수 선언
index = 1

while tower_list:
    # 첫 타워부터 진행
    now_height = tower_list.popleft()
    if not progress:
        # 공정 스택이 비었을 경우 0 추가
        progress.append([now_height, index])
        result.append(0)
    else:
        # 스택에 해당 타워보다 높은 타워가 있는 경우
        # 낮은 타워가 나올 때까지 pop
        if now_height > progress[-1][0]:
            while progress and now_height > progress[-1][0]:
                progress.pop()
            # pop 하다가 전부 제거된 경우 0 추가
            if not progress:
                result.append(0)
            # 아니라면 남은 타워가 수신 타워이므로 index를 결과에 추가
            else:
                result.append(progress[-1][1])
            # 진행 중인 타워를 공정 스택에 추가
            progress.append([now_height, index])
        # 스택 최상단이 현재 타워보다 높은 타워일 경우
        # 바로 직전 타워가 바로 수신한다는 것
        else:
            result.append(progress[-1][1])
            progress.append([now_height, index])
    # 인덱스 1씩 추가
    index += 1

# 결과 리스트 출력
print(*result)