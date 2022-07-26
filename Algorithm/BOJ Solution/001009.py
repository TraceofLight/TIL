import sys
import copy

number = int(input())
output = []
rules = []
for i in range(number) :
    a, b = list(map(int,sys.stdin.readline().split()))
    a = a % 10
    first_a = copy.deepcopy(a)
    while True :
        rules.append(a)
        a = (a * first_a) % 10
        if a in rules :
            break
    output.append(rules[(b % len(rules)) - 1])
    rules = []

for i in range(len(output)) :
    if output[i] == 0 :
        print(10)
        continue
    else :
        print(output[i])