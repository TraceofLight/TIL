import sys

Divisor = int(sys.stdin.readline())
DivisorList = sorted(list(map(int,sys.stdin.readline().split())))

print(DivisorList[0] * DivisorList[-1])