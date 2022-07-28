import sys

number = int(input())
sort_list = []

for i in range(number) :
    x, y = list(map(int,sys.stdin.readline().split()))
    sort_list.append([x, y])

sort_list.sort(key=lambda x: (x[0], x[1]))

for i in range(number) :
    print(*sort_list[i])