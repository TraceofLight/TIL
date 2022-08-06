from collections import deque

number = int(input())
number_list = deque(list(range(1, number + 1)))
counter = number

while counter > 1 :
    number_list.popleft()
    counter -= 1
    if counter == 1 :
        break
    number_list.append(number_list.popleft())

print(number_list.popleft())