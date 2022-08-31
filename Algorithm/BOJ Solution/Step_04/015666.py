# N과 M (12)

import sys
import copy

# n과 m input
number, sequence = map(int, sys.stdin.readline().strip().split())
# 들어오는 n개에 자연수에 대해 중복을 제거하고 dictonary 생성
number_dict = dict(list(enumerate(sorted(list(set(map(int, sys.stdin.readline().split())))))))
# 중복값을 제거한 숫자의 갯수 확인
number = len(number_dict)


# 중복조합 함수 생성
def repetition_c(n, k, number_list, output_list):
    if k == 0:
        output_list.append(copy.deepcopy(number_list))
        return
    last_index = len(number_list) - k - 1
    if len(number_list) == k:
        small_number = 0
    else:
        small_number = number_list[last_index]
    for i in range(small_number, n):
        number_list[last_index + 1] = i
        repetition_c(n, k - 1, number_list)


# 선언한 함수를 통해 n개 중에서 중복 포함 m개를 고른 리스트 생성
hash_list = []
number_hash = [0 for _ in range(sequence)]
repetition_c(number, sequence, number_hash, hash_list)

# 해쉬값에 대응하는 원래 input값으로 리스트를 다시 조합 후 출력
for hash in hash_list:
    output_list = []
    for element in hash:
        output_list.append(number_dict.get(element))
    print(*output_list)
