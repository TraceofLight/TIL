cycle = int(input())
number = input().split()
output = []
if len(number) != cycle :
    exit()
for i in range(len(number)) :
    counter = 1
    if int(number[i]) == 1 :
        continue
    while True :
        counter = counter + 1
        if counter >= int(number[i]) :
            output.append(number[i])
            break
        if int(number[i]) % counter == 0 :
            break
print(len(output))