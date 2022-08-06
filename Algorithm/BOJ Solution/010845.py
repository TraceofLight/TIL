from collections import deque
import sys
number = int(input())
output = deque([])
counter = 0
for i in range(number) :
    command = sys.stdin.readline()
    command = command.rstrip('\n')
    if command.startswith('push') == True :
        c = command.lstrip('push ')
        output.append(int(c))
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
    elif command == 'pop' :
        if counter == 0 :
            print(-1)
        else :
            print(output.popleft())
            counter -= 1
