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



""" 승점이 같은데 등수가 다른 케이스 있어서 폐기
number = int(input())
input_case = []
output_case = []
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

print(*rank)
"""