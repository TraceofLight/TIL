min_number = int(input())
max_number = int(input())
output = []
for i in range(min_number, max_number + 1) :
    counter = 1
    if i == 1 :
        continue
    while True :
        counter = counter + 1
        if counter >= i :
            output.append(i)
            break
        if int(i) % counter == 0 :
            break
if len(output) == 0 :
    print (-1)
else :
    sum = 0
    for j in range(len(output)) :
        sum = sum + output[j]
    print(sum)
    print(min(output))