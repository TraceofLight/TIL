import sys

postfix = []
operator = []
string = sys.stdin.readline().strip('\n')
priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
for chr in string:
    if chr not in ['*', '/', '+', '-', '(', ')']:
        postfix.append(chr)
    else:
        if not operator:
            operator.append(chr)
        else:
            if chr == ')':
                while operator[-1] != '(':
                    postfix.append(operator.pop())
                    if not operator:
                        break
                if operator:
                    operator.pop()
            else:
                while priority.get(chr) <= priority.get(operator[-1]) and operator[-1] != '(':
                    postfix.append(operator.pop())
                    if not operator:
                        break
                operator.append(chr)

while operator:
    postfix.append(operator.pop())

print(''.join(postfix))