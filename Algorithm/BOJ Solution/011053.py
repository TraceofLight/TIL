import sys
from collections import defaultdict

arr_number = int(sys.stdin.readline())
arr_list = list(map(int, sys.stdin.readline().split()))

max_val = [[0, 0], [arr_list[0], 1]]
max_dict = defaultdict(int)
for idx in range(1, arr_number + 1):
    max_dict[idx] = 0
max_length = 0

for idx in range(1, arr_number):
    idx_now = arr_list[idx]
    for element in max_val:
        if element[1] < max_dict[element[0]]:
            continue
        if element[0] < idx_now:
            max_val.append([idx_now, element[1] + 1])
            if element[1] + 1 > max_length:
                max_length = element[1] + 1
                max_dict[idx_now] = max_length

print(max_length)
'hello'