numbers = list(map(int,input().split()))
sum_number = 0

for number in numbers :
    sum_number += number ** 2

print(sum_number % 10)