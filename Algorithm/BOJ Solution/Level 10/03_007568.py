number = int(input())
input_case = []
output_case = []
for i in range(number) :
    a, b = map(int, input().split())
    input_case.append([a, b])

output = []
for i in range(number) : 
    counter = 0
    for j in range(number) :
        if (input_case[i][0] < input_case[j][0]) and input_case[i][1] < input_case[j][1] :
            counter = counter + 1
    counter = counter + 1
    output.append(counter)

print(*output)

"""
number = int(input())
input_case = []
output_case = []
first_input_case = input_case
for i in range(number) :
    input_case.append(input().split())

for i in range(number) : # 리그전 방식 비교 후 가점 부여
    test_case = input_case[i]
    point = 0
    for j in range(number) :
        if test_case[0] > input_case[j][0] and test_case[1] > input_case[j][1] :
            point = point + 1
    output_case.append(point)

rank = [0 for i in output_case]
record = -1
counter = 0
for i in range(number) : # 크기순 정렬
    if record == max(output_case) :
        upper_rank = output_case.index(max(output_case))
        output_case[upper_rank] = -1
        rank[upper_rank] = i - counter
        counter = counter + 1
    else :
        record = max(output_case)
        upper_rank = output_case.index(max(output_case))
        output_case[upper_rank] = -1
        rank[upper_rank] = i + 1
        counter = 0

for i in range(number) : # 동일 등수 내 정렬
    list_overlap = list(filter(lambda x: rank[x] == i, range(number)))
    if len(list_overlap) >= 2 :
        for j in list_overlap :
            for k in list_overlap :
                if input_case[j][0] > input_case[k][0] and input_case[j][1] > input_case[k][1] :
                    rank[k] = rank[k] + 1

print(*rank)

number = int(input())
input_case = []
output_case = []
for i in range(number) :
    input_case.append(input().split())

rank = []
for i in range(number) :
    if i == 0 :
        rank.append(input_case[0])
    else :
        for j in range(len(rank)) :
            if input_case[i][0] > rank[j][0] and input_case[i][1] > rank[j][1] :
                rank.insert(j, input_case[i])
                break
            elif j == len(rank) - 1 :
                rank.append(input_case[i])
print(rank)

rank_number = [0 for i in input_case]
counter = 1
for i in range(number) :
    rank_number[i] = rank.index(input_case[i]) + 1
    if i != 0 :
        if rank[i][0] >= rank[i - 1][0] or rank[i][1] >= rank[i - 1][1] :
            rank_number[i] = rank.index(input_case[i]) - counter
            counter = counter + 1
    else :
        counter = 1
        continue
print(rank_number)
        if input_case[record][0] > input_case[upper_rank][0] and input_case[record][1] > input_case[upper_rank][1] :
            rank[upper_rank] = rank[upper_rank] + 1
"""