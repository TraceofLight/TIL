import sys

number = int(input())
number_list = list(map(int,sys.stdin.readline().split()))
result = []
stack = []
max_number = float('-inf')

while number_list:
    if not result:
        result.append(-1)
        max_number = number_list.pop()
        stack.append(max_number)
    else:
        top_number = number_list.pop()
        if top_number >= max_number:
            max_number = top_number
            stack.append(max_number)
            result.append(-1)
        elif top_number >= stack[-1]:
            while stack[-1] <= top_number:
                stack.pop()
            result.append(stack[-1])
            stack.append(top_number)
        else:
            result.append(stack[-1])
            stack.append(top_number)

for idx in range(number - 1, -1, -1):
    print(result[idx], end=' ')
