from collections import deque
import sys
number = int(input())
output = deque([])
counter = 0
for i in range(number) :
    command = sys.stdin.readline()
    command = command.rstrip('\n')
    if command.startswith('push_front') == True :
        command = command.lstrip('push_front ')
        output.appendleft(int(command))
        counter += 1
    if command.startswith('push_back') == True :
        command = command.lstrip('push_back ')
        output.append(int(command))
        counter += 1
    elif command == 'front' :
        if counter == 0 :
            print(-1)
        else :
            a = output.popleft()
            print(a)
            output.appendleft(a)
        continue
    elif command == 'back' :
        if counter == 0 :
            print(-1)
        else :
            b = output.pop()
            print(b)
            output.append(b)
    elif command == 'size' :
        print(counter)
    elif command == 'empty' :
        if counter == 0 :
            print(1)
        else :
            print(0)
    elif command.startswith('pop_front') == True :
        command = command.lstrip('pop_front ')
        if counter == 0 :
            print(-1)
        else :
            print(output.popleft())
            counter -= 1
    elif command.startswith('pop_back') == True :
        command = command.lstrip('pop_back ')
        if counter == 0 :
            print(-1)
        else :
            print(output.pop())
            counter -= 1
