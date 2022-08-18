import sys

factorial_list = [1]
def factorial(val):
    global factorial_list
    length = len(factorial_list)
    if val <= length:
        return factorial_list[val - 1]
    else:
        for idx in range(length, val):
            factorial_list.append(factorial_list[idx - 1] * (idx + 1))
        return factorial_list[val - 1]

n, m = map(int, sys.stdin.readline().split())

print(factorial(n) // factorial(n - m) // factorial(m))