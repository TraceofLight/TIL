import sys

n, m, b = list(map(int, sys.stdin.readline().split()))

total_ground = n * m
ground_info = []
sum_ground = 0
max_ground = '#'
for arr_y in range(n) :
    line = list(map(int,sys.stdin.readline().split()))
    for arr_x in range(m) :
        ground_info.append(line[arr_x])
        sum_ground += line[arr_x]
        if max_ground == '#' :
            max_ground = line[arr_x]
        elif max_ground < line[arr_x] :
            max_ground = line[arr_x]

total_result = []

for i in range(0, max_ground + 1) :
    total_time = 0
    if sum_ground + b < m * n * i :
        continue
    for ground in ground_info :
        if ground >= i :
            total_time += (ground - i) * 2
        else :
            total_time += (i - ground)
    if i == 0 :
        total_result = [total_time, i]
    else :
        if total_result[0] >= total_time :
            total_result = [total_time, i]

print(*total_result)
