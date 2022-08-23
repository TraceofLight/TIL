import sys

operend = int(sys.stdin.readline())
postfix = sys.stdin.readline().strip('\n')

operend_list = []
for idx in range(operend):
    operend_list.append([chr(65 + idx), int(sys.stdin.readline().strip('\n'))])
operend_dict = dict(operend_list)

stack1 = ['#']
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in postfix:
    if letter in '*/+-':
        num2 = stack1.pop()
        if str(num2) in alphabet:
            num2 = operend_dict.get(num2)
        num1 = stack1.pop()
        if str(num1) in alphabet:
            num1 = operend_dict.get(num1)
        if letter == '*':
            stack1.append(num1 * num2)
        if letter == '/':
            stack1.append(num1 / num2)
        if letter == '+':
            stack1.append(num1 + num2)
        if letter == '-':
            stack1.append(num1 - num2)
    else:
        stack1.append(letter)

print(f'{stack1[1]:.2f}')