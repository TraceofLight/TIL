import sys

number = int(input())
group = list(map(int,sys.stdin.readline().split()))
output_list = []

for i, element in enumerate(group) :
    output_list.append([element, i])

output_list.sort(key= lambda x: x[0])

counter = 0
for i in range(number) :
    output_list[i].append(counter)
    try :
        if memorized[0] == output_list[i][0] :
            output_list[i][2] = memorized[2]
            counter -= 1
    except :
        pass
    memorized = output_list[i]
    counter += 1

output_list.sort(key= lambda x: x[1])

output = [i[2] for i in output_list]

print(*output)