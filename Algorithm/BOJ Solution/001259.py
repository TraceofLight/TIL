output = []

while True :
    checker = True
    numbers = list(input())

    if numbers == ['0'] :
        break

    for i in range(len(numbers) // 2) :
        if numbers.pop(0) != numbers.pop() :
            output.append('no')
            checker = False
            break
        
    if checker == True :
        output.append('yes')

print(*output, sep = '\n')