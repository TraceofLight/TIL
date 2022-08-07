from math import sqrt
import sys

def prime(a) :
    if a == 1 :
        return False
    for i in range(2, int(sqrt(a)) + 1) :
        if a % i == 0 :
            return False
    return True

output = []

while True :
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    counter = 0
    for i in range(n + 1, 2 * n + 1) :
        if prime(i) :
            counter += 1
    output.append(counter)

print(*output, sep = '\n')