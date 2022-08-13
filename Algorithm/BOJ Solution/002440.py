import sys

number = int(sys.stdin.readline())

for i in range(number):
    print('*' * (number - i))