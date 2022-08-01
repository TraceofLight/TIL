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
'''