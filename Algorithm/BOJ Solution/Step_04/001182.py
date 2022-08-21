import sys

number, sum_number = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
counter = 0
result = 0

for bit in range(1, 1 << number):
    counter += 1
    subset = []
    for idx in range(number):
        if bit & (1 << idx):
            subset.append(number_list[idx])
    if sum(subset) == sum_number:
        result += 1

print(result)