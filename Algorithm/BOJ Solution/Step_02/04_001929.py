from math import sqrt

def prime(a) :
    if a == 1 :
        return False
    for i in range(2, int(sqrt(a)) + 1) :
        if a % i == 0 :
            return False
    return True

m, n = list(map(int,input().split()))

for i in range(m, n + 1) :
    if prime(i) :
        print(i)