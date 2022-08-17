import sys

number = int(sys.stdin.readline())
time_list = sorted(list(map(int, sys.stdin.readline().split())))
sum_time = sum(time_list)
result = 0
for _ in range(number):
    result += sum_time
    sum_time -= time_list.pop()

print(result)