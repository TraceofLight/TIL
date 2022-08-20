import sys
import copy

number, sequence = map(int, sys.stdin.readline().strip().split())
number_dict = dict(list(enumerate(sorted(list(set(map(int, sys.stdin.readline().split())))))))
number = len(number_dict)

hash_list = []

def repetition_c(n, k, number_list):
    global hash_list
    if k == 0:
        hash_list.append(copy.deepcopy(number_list))
        return
    last_index = len(number_list) - k - 1
    if len(number_list) == k:
        small_number = 0
    else:
        small_number = number_list[last_index]
    for i in range(small_number, n):
        number_list[last_index + 1] = i
        repetition_c(n, k - 1, number_list)

number_hash = [0 for _ in range(sequence)]
repetition_c(number, sequence, number_hash)

for hash in hash_list:
    output_list = []
    for element in hash:
        output_list.append(number_dict.get(element))
    print(*output_list)