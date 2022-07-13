import sys
from collections import *

number = int(input())
counter = 0
number_list = [0 for i in range(10001)]

for i in range(number) :
    counter += 1
    input_number = int(sys.stdin.readline())
    number_list[input_number] += 1

for i in range(len(number_list)) :
    while number_list[i] != 0 :
        print(i)
        number_list[i] -= 1

"""
방법 1

number = int(input())
list_number = []
for i in range(number) :
    list_number.append(int(sys.stdin.readline()))
list_number.sort()

print(*list_number, sep ='\n')

방법 2

b = Counter(a).most_common()
c = sorted(b, key = lambda x : x[0]) 
d = []

for i in range(len(c)) :
    d.append(list(c[i]))

for i in range(len(d)) :
    for j in range(d[i][1]) :
        print(d[i][0])
"""