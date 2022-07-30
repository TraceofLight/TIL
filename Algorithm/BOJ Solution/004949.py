output = []
counter = 0
brakets = ['a', 'b', 'c', 'd']
checker = True

while True:
    status =''
    input_string = input()
    if input_string == '.' :
        break
    for letter in input_string :
        if letter == '[' :
            status = status + 'a'
        elif letter == ']' :
            status = status + 'b'
        elif letter == '(' :
            status = status + 'c'
        elif letter == ')' :
            status = status + 'd'
    while status.find('ab') != -1 or status.find('cd') != -1 :
        while status.find('ab') != -1 :
            status = status.replace('ab', '')
        while status.find('cd') != -1 :
            status = status.replace('cd', '')
    while status.find('a') < status.rfind('b') and status.find('a') != -1 :
            status = status.replace('a', '')
            status = status[::-1]
            status = status.replace('b', '')
            status = status[::-1]
    while status.find('c') < status.rfind('d') and status.find('a') != -1 :
            status = status.replace('c', '')
            status = status[::-1]
            status = status.replace('d', '')
            status = status[::-1]
    if len(status) > 0 :
        output.append('no')
        continue
    output.append('yes')

print(*output, sep = '\n')
