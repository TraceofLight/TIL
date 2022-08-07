number = int(input())
complete = []
for i in number :
    complete.append(int(input()))
stack1 = []
output = []
counter = 0

while output != complete :
    for i in range(number) :
        counter = 1
        while counter != complete[i] :
            stack1.append(i)
            print('+')
            counter += 1
        counter = 0
        while stack1[-1] == complete[i + counter] :
            output.append(stack1.pop())
            print('-')
            counter += 1
    stack1.append
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
