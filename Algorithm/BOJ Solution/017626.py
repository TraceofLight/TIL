import sys
from math import sqrt

number = int(sys.stdin.readline())
sqrt_number = int(sqrt(number))

multiple_group = []
for num in range(1, sqrt_number + 1):
    multiple_group.append(num ** 2)

for multiple in multiple_group:
    if number == multiple:
        print(1)
        exit()

for idx1 in range(sqrt_number):
    for idx2 in range(sqrt_number):
        if number == multiple_group[idx1] + multiple_group[idx2]:
            print(2)
            exit()

for idx1 in range(sqrt_number):
    for idx2 in range(sqrt_number):
        for idx3 in range(sqrt_number):
            if number == multiple_group[idx1] + multiple_group[idx2] + multiple_group[idx3]:
                print(3)
                exit()

print(4)