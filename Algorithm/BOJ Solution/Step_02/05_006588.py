import sys
from math import sqrt

# 소수 체크 함수
def prime(a) :
    if a == 1 :
        return False
    for i in range(2, int(sqrt(a)) + 1) :
        if a % i == 0 :
            return False
    return True

# 결과물 arr 형성
output = []

# 0이 나오기 전까지 반복
while True :
    target = int(sys.stdin.readline())
    if target == 0 :
        break
    half = target // 2 
    counter = 3
    while True :
        # 소수를 만날 경우?
        if prime(counter) :
            # 타겟값에서 해당 소수를 뺀 수도 소수인 경우 arr 반영
            if prime(target - counter) :
                output.append([target, counter, target - counter])
                break
        # 2만큼 증감 시 홀수만 잡힘
        counter += 2

for element in output :
    print(element[0], '=', element[1], '+', element[2])