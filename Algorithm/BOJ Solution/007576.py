import sys

width, height = map(int, sys.stdin.readline().split())
box = []
for _ in range(height):
    box.append(list(map(int, sys.stdin.readline().split())))