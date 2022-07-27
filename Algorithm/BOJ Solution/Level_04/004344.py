testcase = int(input())
output = []
for k in range(testcase) :
    score = input().split()
    sum = 0
    overaverage = []
    for i in range(1, len(score)) :
        sum = sum + int(score[i])
    average = sum / (len(score) - 1)
    for j in range(1, len(score)) :
        if int(score[j]) > average :
            overaverage.append(score[j])
    output.append(format(len(overaverage)/(len(score) - 1) * 100, ".3f"))
for l in range(len(output)) :
    print(output[l],'%', sep ='')