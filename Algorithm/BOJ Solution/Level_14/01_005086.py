import sys

output = []

while True:
    num1, num2 = map(int, sys.stdin.readline().split())
    if not num1 and not num2:
        break
    if num2 % num1 == 0:
        output.append('factor')
    elif num1 % num2 == 0:
        output.append('multiple')
    else:
        output.append('neither')

for result in output:
    print(result)