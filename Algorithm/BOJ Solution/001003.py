import sys
counter = []

def fibonacci(a) :
    if a == 0 :
        counter.append(0)
    if a == 1 :
        counter.append(1)
    return fibonacci(a - 1) + fibonacci(a - 2)

number = int(input())
for i in range(number) :
    x = int(sys.stdin.readline())
    fibonacci(x)