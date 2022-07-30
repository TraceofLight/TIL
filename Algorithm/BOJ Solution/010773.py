import sys

number = int(input())
output = []

for i in range(number) :
    input_number = int(sys.stdin.readline())
    if input_number == 0 :
        output.pop(-1)
    else :
        output.append(input_number)

print(sum(output))