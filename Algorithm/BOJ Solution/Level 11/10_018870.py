import sys

number = int(input())
group = list(map(int,sys.stdin.readline().split()))
length = len(group)
output = [0 for i in range(length)]
new_group = [i for i in group]
new_group.sort()
memory = 0

for i in range(len(group)) :
    idx_group = group.index(new_group[i]) 
    if new_group[i] == new_group[i - 1] :
        output[idx_group] = memory
    else :
        output[idx_group] = i
        memory = i
    group[idx_group] ='#'

print(*output)
