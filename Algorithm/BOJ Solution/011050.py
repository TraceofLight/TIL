n, k = list(map(int,input().split()))

def factorial(a, b) :
    if a == 1 :
        return 1
    elif b == 0 :
        return 1
    return a * factorial(a - 1, b - 1)
print(int((factorial(n, k))/(factorial(k, k))))