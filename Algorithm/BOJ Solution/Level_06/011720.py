a = int(input())
b = input()
c = list(b)
sum = 0
if len(c) != a :
    exit()
d = [int(i) for i in c]
for i in range(len(d)) :
    sum = sum + d[i]
print(sum)