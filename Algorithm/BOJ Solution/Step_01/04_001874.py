number = int(input())
stack1 = []
output = []
for i in range(number) :
    stack1.append(int(input()))

for i in range(number) :
    while number != output[i] :
        stack1.append(i)
    if number == 0:
        pass

        while stack1[i] > number :
            number += 1
        output.append(number)
    elif stack1[i] < number :
        while True:
            pass
    number += 1
    43687
    125
    12578
    436
