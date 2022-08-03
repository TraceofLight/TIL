import sys

word = list(enumerate(sys.stdin.readline()))
print(word)
commandLine = int(sys.stdin.readline())
length = len(word)
cursor = length
memory = []
memory_cursor = []
counter = 0
for i in range(commandLine) :
    inputCommand = sys.stdin.readline()
    if inputCommand == 'L' :
        if cursor == 0 :
            continue
        else :
            cursor -= 1
    elif inputCommand == 'D' :
        if cursor == length :
            continue
        else :
            cursor += 1
    elif inputCommand == 'B' : 
        if cursor == 0 :
            continue
        else :
            word.pop(cursor)
            cursor -= 1
    elif inputCommand.startswith('P') == True :
        real_input = inputCommand.lstrip('P ')
        memory.append(real_input)
        memory_cursor.append(real_input)
        cursor = cursor + len(real_input)
        print(memory, memory_cursor)

for i in len(word) :
    print(word[i], sep = '', end = '')
    if i in memory_cursor :
        counter += 1
        print(memory[counter - 1], sep = '', end = '')

'''
word = list(input())
commandLine = int(input())
cursor = len(word)

for i in range(commandLine) :
    inputCommand = input()
    if inputCommand == 'L' :
        if cursor == 0 :
            continue
        else :
            cursor -= 1
    elif inputCommand == 'D' :
        if cursor == len(word) :
            continue
        else :
            cursor += 1
    elif inputCommand == 'B' : 
        if cursor == 0 :
            continue
        else :
            list_word = list(word)
            list_word.pop(cursor)
            word = str(list_word)
            cursor -= 1
    elif inputCommand.startswith('P') == True :
        real_input = inputCommand.lstrip('P ')
        list_word = list(word)
        list_word.insert(cursor, real_input)
        word = ''.join(list_word)
        cursor = cursor + len(real_input)

print(word)

import sys
from collections import deque

word = deque(list(sys.stdin.readline()))
word.pop()
commandLine = int(input())
length = len(word)
cursor = length
for i in range(commandLine) :
    command = input()
    command = command.rstrip('\n')
    if command == 'L' :
        if cursor == 0 :
            continue
        else :
            cursor -= 1
    elif command == 'D' :
        if cursor == length :
            continue
        else :
            cursor += 1
    elif command == 'B' : 
        if cursor == 0 :
            continue
        else :
            tmp = []
            for i in range(length - cursor) :
                tmp.append(word.pop())
            word.pop()
            for i in range(length - cursor) :
                word.append(tmp.pop())
            cursor -= 1
            length -= 1
    elif command.startswith('P ') :
        command = command.lstrip('P ')
        tmp = []
        for i in range(cursor, length) :
            tmp.append(word.pop())
            command_counter = 0
        for letter in command :
            word.append(letter)
            command_counter += 1
        for i in range(length - cursor) :
            word.append(tmp.pop())
        length += command_counter
        cursor += command_counter
        continue

print(*word, sep ='')

'''