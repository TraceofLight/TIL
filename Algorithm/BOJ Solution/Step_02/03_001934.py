import sys

testCase = int(input())
output = []

for i in range(testCase) :
    a, b = list(map(int,sys.stdin.readline().split()))
    counter = 2
    commonFactor = 1
    commonMultiple = 1
    while a != 1 and b != 1 :
        remainder_a = a % counter
        remainder_b = b % counter 
        if remainder_a == 0 and remainder_b == 0 :
            a = a // counter 
            b = b // counter
            commonFactor *= counter
            continue
        elif remainder_a == 0 :
            a = a // counter
            commonMultiple *= counter
            continue
        elif remainder_b == 0 :
            b = b // counter
            commonMultiple *= counter
            continue
        counter += 1
    result = commonFactor * commonMultiple * a * b
    output.append(result)

print(*output, sep = '\n')