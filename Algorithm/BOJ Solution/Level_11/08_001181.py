import sys

number = int(input())
word_list = []

for i in range(number) :
    x = sys.stdin.readline()
    word_list.append(x)

output = list(set(word_list))
output.sort(key=lambda x: (len(x), x))

for i in range(len(output)) :
    print(*output[i], sep ='', end = '')