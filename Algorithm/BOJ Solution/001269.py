import sys

GroupANumber, GroupBNumber = list(map(int,sys.stdin.readline().split()))

GroupA = set(map(int,sys.stdin.readline().split()))
GroupB = set(map(int,sys.stdin.readline().split()))

SymmetricDifference = len(GroupA ^ GroupB)

print(SymmetricDifference)