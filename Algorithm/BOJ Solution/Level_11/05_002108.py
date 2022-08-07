import sys
from collections import *

number = int(input())
number_list = []
for i in range(number) :
    number_list.append(sys.stdin.readline())
new_list = [int(i) for i in number_list]
new_list.sort()

# 산술평균
a = round(sum(new_list) / len(new_list))

# 중앙값
b = new_list[(len(new_list) - 1)// 2]

# 최빈값

count_list_ = Counter(new_list).most_common()
count_list = []
for i in range(len(count_list_)) :
    count_list.append(list(count_list_[i]))
cnt = []
for i in range(len(count_list)) :
    cnt.append(count_list[i][1])
standard = count_list[0][1]
cnt_list = []
for i in range(len(count_list)) :
    if cnt[i] == standard :
        cnt_list.append(count_list[i][0])
if len(cnt_list) == 1 :
    c = cnt_list[0]
else :
    cnt_list.sort()
    c = cnt_list[1]

# 범위
d = new_list[-1] - new_list[0]

output = [a, b, c, d]
for i in range(len(output)) :
    if output[i] == -0 :
        output[i] = 0
    print(output[i])

""" enumerarte 활용 최빈값 계산
for i in range(len(for_c)) :
    count_max.append(new_list.count(for_c[i]))
print(count_max)
real_max = max(count_max)
c = for_c[count_max.index(real_max)]
if count_max.count(real_max) != 1 :
    max_index = [i for i, value in enumerate(count_max) if value == real_max]
    max_list = []
    for i in range(len(max_index)) :
        max_list.append(for_c[i])
    max_list.sort()
    c = max_list[1]
"""