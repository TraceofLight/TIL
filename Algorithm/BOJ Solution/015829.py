import sys

length = int(input())
word = list(sys.stdin.readline().strip())
counter = 0
output = 0

while length != 0 :
    output += (ord(word[counter]) - 96) * (31 ** counter)
    counter += 1
    length -= 1

print(output % 1234567891)