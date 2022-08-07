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

# 테스트 횟수 및 결과물 arr 형성
testCase = int(sys.stdin.readline())
output = []

# 횟수만큼 반복
for i in range(testCase) :
    target = int(sys.stdin.readline())
    half = target // 2 
    counter = 0
    # 중간부터 하나씩 빼면서 소수를 만날 경우?
    while True :
        if prime(half - counter) :
            # 타겟값에서 해당 소수를 뺀 수도 소수인 경우 arr 반영
            if prime(target - (half - counter)) :
                output.append([half - counter, target - (half - counter)])
                break
        counter += 1

for element in output :
    print(*element)