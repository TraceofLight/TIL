from itertools import combinations

input_1 = input().split()
input_2 = input().split()

card_number = int(input_1[0])
maximum = int(input_1[1])
list_ = [int(i) for i in input_2]
combination_list = list(combinations(list_, 3))
sum_list = []
for i in range(len(combination_list)) :
    sum_list.append(sum(combination_list[i]))

output = [i for i in sum_list if i <= maximum]
print(max(output))