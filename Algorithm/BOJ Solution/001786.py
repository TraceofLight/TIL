# KMP 알고리즘

import sys

string = sys.stdin.readline().strip('\n')
find_this_string = sys.stdin.readline().strip('\n')
length_string = len(string)
length_find_string = len(find_this_string)

prefix_suffix = [0 for _ in range(length_find_string)]
# 순환 사이클이 깨졌을 때 어디부터 시작할지?
longest = 0
index = 1
while index < length_find_string:
    # 같은 경우 인덱스 전체 1개 더 증가
    if find_this_string[index] == find_this_string[longest]:
        longest += 1
        prefix_suffix[index] = longest
        index += 1
    else:
        # 0 이 아니라면 줄여서 체크
        if longest != 0:
            longest = prefix_suffix[longest - 1]
        # 0 이면 처음부터 검색
        else:
            prefix_suffix[index] = 0
            index += 1

string_index = 0
find_this_string_index = 0
result = 0
result_list = []

while string_index < length_string:
    if string[string_index] == find_this_string[find_this_string_index]:
        string_index += 1
        find_this_string_index += 1
    else:
        if find_this_string_index == 0:
            string_index += 1
        else:
            find_this_string_index = prefix_suffix[find_this_string_index - 1]
    if find_this_string_index == length_find_string:
        result += 1
        result_list.append(string_index - length_find_string + 1)
        find_this_string_index = prefix_suffix[-1]

print(result)
print(*result_list)
