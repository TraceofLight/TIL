from collections import deque

n, k = list(map(int,input().split()))

counter = 0
real_count = 0
calc = 0
number_list = deque(list(range(1, n + 1)))
output = []
while real_count != n :
    a = number_list.popleft()
    counter += 1
    if counter % k == 0 :
        output.append(a)
        real_count += 1
    else :
        number_list.append(a)

print('<', end = '')
for i in range(n - 1) :
    print(output[i], end = ', ')
print(output.pop(), end = '')
print('>', end = '')