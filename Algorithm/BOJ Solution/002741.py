import sys

a = int(sys.stdin.readline())
b = [i for i in range(1, a+1)]

print(*b, sep = '\n')