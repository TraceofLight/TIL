import sys

class Node :
    def __init__(self, data=None) :
        self.data = data
        self.nextval = None

class Linkedlist :
    def __init__(self) :
        extra = Node('extra')
        self.head = extra
        self.tail = extra
        self.current = None
        self.before = None

    def listprint(self) :
        printval = self.headval
        while printval is not None :
            print(*printval.data, end = '')
            printval = printval.nextval

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node


    def delete(self):
        pop_data = self.current.data
        if self.current is self.tail:
            self.tail = self.before
        self.before.next = self.current.next
        self.current = self.before
        return pop_data

    def forward(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def back(self):
        if self.current.before == None:
            return None
        self.current = self.before
        self.current.next = self.current

        return self.current.data

word_unrefined = sys.stdin.readline()
word_unrefined.rstrip(' \n')
word = list(word_unrefined)
commandLine = int(sys.stdin.readline())
length = len(word)
cursor = length
counter = 0

Linkedlist1 = Linkedlist()

for letter in word :
    Linkedlist1.append(letter)

for node in Linkedlist1 :
    print(node.data)

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