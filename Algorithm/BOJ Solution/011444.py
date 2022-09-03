# 피보나치 수 6

import sys
from collections import defaultdict


# 피보나치 수열을 행렬연산하는 함수 선언
def fibonacci(number, dict:dict):
    if number <= 1:
        return [[1, 1], [1, 0]]
    else:
        # 기존에 이미 구한 값이 있을 경우 해당 값을 반환
        if dict.get(number) is not None:
            return dict[number]
        # 그렇지 않을 경우 피보나치 연산을 수행
        # 숫자가 계속 커지므로 중간에 나머지 연산 추가
        else:
            arr = [[0, 0], [0, 0]]
            arr_a = fibonacci(number // 2, dict)
            arr_b = fibonacci(number - (number // 2), dict)
            arr[0][0] = (arr_a[0][0] * arr_b[0][0] + arr_a[0][1] * arr_b[1][0]) % 1000000007
            arr[0][1] = (arr_a[0][0] * arr_b[0][1] + arr_a[0][1] * arr_b[1][1]) % 1000000007
            arr[1][0] = (arr_a[1][0] * arr_b[0][0] + arr_a[1][1] * arr_b[1][0]) % 1000000007
            arr[1][1] = (arr_a[1][0] * arr_b[0][1] + arr_a[1][1] * arr_b[1][1]) % 1000000007
            dict[number] = arr
            return arr

# number input
number = int(sys.stdin.readline())

# 2보다 작다면 기본값을 출력하고 그 외에 값에 대해선 함수를 실행하여 값을 출력
if number <= 2:
    print(1)
else:
    data_dict = defaultdict(int)
    result_list = fibonacci(number - 1, data_dict)
    print((result_list[0][1] + result_list[1][1]) % 1000000007)


'''
# 피보나치 점화식

f(n) = f(n-1) + f(n-2)

해당 점화식을 통하여 행렬 연산으로 치환이 가능

|f(n+1)| = | 1 1 | * |f(n)  | 
|f(n)  |   | 1 0 |   |f(n-1)|

|f(n+1)| = | 1 1 | ^ n * |f(1)|
|f(n)  |   | 1 0 |       |f(0)|

'''
