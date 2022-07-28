import sys

testData = int(input())
output = []

for i in range(testData) :
    list_vps = list(sys.stdin.readline())
    counter = 0
    for element in list_vps :
        if element == '(' :
            counter += 1
        elif element == ')' :
            counter -= 1
        if counter < 0 :
            counter = '#'
            break
    if counter == 0 :
        output.append('YES')
    else :
        output.append('NO')

print(*output, sep = '\n')