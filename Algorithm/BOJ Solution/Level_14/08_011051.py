import sys

factorial_list = [1]

def factorial(val):
    global factorial_list
    length = len(factorial_list)
    if val <= length - 1:
        return factorial_list[val]
    else:
        for idx in range(length, val + 1):
            factorial_list.append(factorial_list[idx - 1] * idx)
        return factorial_list[val]

n, k = list(map(int, sys.stdin.readline().split()))

print(((factorial(n) // factorial(n - k)) // factorial(k)) % 10007)