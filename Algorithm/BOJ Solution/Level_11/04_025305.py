import sys

n, k = list(map(int,sys.stdin.readline().split()))
scores = list(map(int,sys.stdin.readline().split()))

scores.sort()
print(scores[-k])