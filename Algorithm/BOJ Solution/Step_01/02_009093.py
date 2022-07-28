import sys

testCase = int(input())

output = []
for i in range(testCase) :
    word_list = sys.stdin.readline().split()
    word_list = [''.join(reversed(list(word))) for word in word_list]
    output.append(word_list)

for i in range(len(output)) :
    print(*output[i])
