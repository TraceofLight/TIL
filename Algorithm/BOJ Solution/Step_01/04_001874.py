import sys

number = int(input())
arr_target = []
stack1 = []
stack_result = []
output = []
counter = 0
stack_length = 0
length = number
checker = False

for i in range(number) :
    arr_target.append(int(sys.stdin.readline()))

rev_arr_target = list(reversed(arr_target))

while length != 0 :
    while counter < rev_arr_target[-1] :
        counter += 1
        stack1.append(counter)
        stack_length += 1
        output.append('+')
        if counter > number :
            checker == True
            break
    if rev_arr_target[-1] < stack1[-1] :
        checker = True
    if checker == True :
        break
    while rev_arr_target[-1] == stack1[-1] and length != 0 :
        stack_result.append(stack1.pop())
        rev_arr_target.pop()
        length -= 1
        stack_length -= 1
        output.append('-')
        if length == 0 or stack_length == 0 :
            break

if checker == False and stack_result == arr_target :
    print(*output, sep = '\n')
else :
    print('NO')