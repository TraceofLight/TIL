import sys

number = int(input())
member_list = []
for i in range(number) :
    a, b = sys.stdin.readline().split()
    member_list.append([int(a), b])

sort_list = sorted(member_list, key = lambda x : x[0]) 

for i in range(number) :
    print(*sort_list[i], sep =' ')