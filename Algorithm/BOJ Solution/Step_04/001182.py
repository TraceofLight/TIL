# 부분수열의 합

import sys

# 정수 갯수, 목표 합값, 정수 리스트 input
number, sum_number = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
counter = 0
result = 0

# 1부터 2^(number)까지의 수를 비트로 표현
for bit in range(1, 1 << number):
    counter += 1
    subset = []
    for idx in range(number):
        # 비트 n번째 자리에 1이 있을 경우 부분집합에도 해당 주소의 값 추가
        if bit & (1 << idx):
            subset.append(number_list[idx])
    # 부분집합이 조건을 만족할 경우 결과값 1 추가
    if sum(subset) == sum_number:
        result += 1

# 결과값 출력
print(result)
