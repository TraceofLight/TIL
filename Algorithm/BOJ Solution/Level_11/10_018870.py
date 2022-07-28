import sys

number = int(input())
group = list(map(int,sys.stdin.readline().split()))
output = []

for i, element in enumerate(group) :
    output.append([element, i])

output.sort(key= lambda x: x[0])

counter = 0
for i in range(number) :
    output[i].append(counter)
    try :
        if memorized[0] == [output][i][0] :
            output[i][2] == memorized[2]
        

    memorized = output[i]


for element in output :
    for other_element in output
    if element[0] == other_element[0]

output.sort(key= lambda x: x[1])

print(output)