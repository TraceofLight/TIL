scales = list(map(int,input().split()))
output = []

for i in range(7) :
    output.append(scales[i + 1] - scales[i])

if output.count(1) == 7 :
    print('ascending')
elif output.count(-1) == 7 :
    print('descending')
else :
    print('mixed')