from collections import deque
import sys

# 커서를 기준으로 리스트와 덱을 분할
text = list(sys.stdin.readline().strip())
commandline = int(sys.stdin.readline().strip())
text_right = deque([])

# 리스트의 top, 덱의 bottom 의 pop, append 로 커서 구현
for i in range(commandline):
    command = sys.stdin.readline().strip()
    if command.startswith('L')== True :
        try :
            letter = text.pop()
            text_right.appendleft(letter)
        except :
            continue

    elif command.startswith('D') == True :
        try :
            letter = text_right.popleft()
            text.append(letter)
        except :
            continue

    elif command.startswith('B') == True :
        try :
            text.pop()
        except :
            continue

    elif command.startswith('P')== True :
        text.append(command.lstrip('P '))

# 출력은 덱과 리스트를 이은 뒤 string화
print(''.join(text + list(text_right)))

'''
import sys

class Node :
    def __init__(self, data = None, nextData = None) :
        self.data = data
        self.previous = self
        self.next = self

class Linkedlist :
    def __init__(self) :
        self.init = Node()
        self.head = self.init
        self.tail = self.init
        self.current = self.tail

    def printList(self) :
        node = self.head
        while node :
            print(node.data, end = '')
            node = node.next

    def delete(self):
        if self.current is self.tail:
            self.tail = self.current.previous
            return None
        elif self.current is self.head:
            self.head = self.current.next
            return None
        self.current = self.current.previous
        self.current.next = self.current.next.next
        self.current.next.next.previous = self.current

    def append(self, data):
        insert_node = Node(data)
        if self.head == self.init :
            self.head == insert_node
        self.tail.next = insert_node
        insert_node.previous = self.tail
        self.tail = insert_node

    def insert(self, data):
        insert_node = Node(data)
        if self.current is self.head :
            self.current.next = insert_node
            insert_node.previous = self.current
            return None
        elif self.current is self.tail :
            self.append(data)
            return None
        self.current.next = insert_node
        insert_node.next = self.current.next
        self.current.next.previous = insert_node
        insert_node.previous = self.current

    def forward(self):
        if self.current == self.tail:
            return None
        self.current = self.current.next

    def back(self):
        if self.current == self.head:
            return None
        self.current = self.current.previous

word_unrefined = sys.stdin.readline()
word_unrefined = word_unrefined.rstrip('\n')
word = list(word_unrefined)
commandLine = int(sys.stdin.readline())

Linkedlist1 = Linkedlist()

for letter in word :
    Linkedlist1.append(letter)

for i in range(commandLine) :
    inputCommand = sys.stdin.readline()
    inputCommand = inputCommand.strip('\n')
    if inputCommand == 'L' :
        Linkedlist1.back()
    elif inputCommand == 'D' :
        Linkedlist1.forward()
    elif inputCommand == 'B' : 
        Linkedlist1.delete()
    elif inputCommand.startswith('P') == True :
        real_input = inputCommand.lstrip('P ')
        for letter in real_input :
            Linkedlist1.insert(letter)

Linkedlist1.printList()

word = list(input())
commandLine = int(input())
text_right = len(word)

for i in range(commandLine) :
    inputCommand = input()
    if inputCommand == 'L' :
        if text_right == 0 :
            continue
        else :
            text_right -= 1
    elif inputCommand == 'D' :
        if text_right == len(word) :
            continue
        else :
            text_right += 1
    elif inputCommand == 'B' : 
        if text_right == 0 :
            continue
        else :
            list_word = list(word)
            list_word.pop(text_right)
            word = str(list_word)
            text_right -= 1
    elif inputCommand.startswith('P') == True :
        real_input = inputCommand.lstrip('P ')
        list_word = list(word)
        list_word.insert(text_right, real_input)
        word = ''.join(list_word)
        text_right = text_right + len(real_input)

print(word)

import sys
from collections import deque

word = deque(list(sys.stdin.readline()))
word.pop()
commandLine = int(input())
length = len(word)
text_right = length
for i in range(commandLine) :
    command = input()
    command = command.rstrip('\n')
    if command == 'L' :
        if text_right == 0 :
            continue
        else :
            text_right -= 1
    elif command == 'D' :
        if text_right == length :
            continue
        else :
            text_right += 1
    elif command == 'B' : 
        if text_right == 0 :
            continue
        else :
            tmp = []
            for i in range(length - text_right) :
                tmp.append(word.pop())
            word.pop()
            for i in range(length - text_right) :
                word.append(tmp.pop())
            text_right -= 1
            length -= 1
    elif command.startswith('P ') :
        command = command.lstrip('P ')
        tmp = []
        for i in range(text_right, length) :
            tmp.append(word.pop())
            command_counter = 0
        for letter in command :
            word.append(letter)
            command_counter += 1
        for i in range(length - text_right) :
            word.append(tmp.pop())
        length += command_counter
        text_right += command_counter
        continue

print(*word, sep ='')

'''