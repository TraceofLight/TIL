output = []

while True :
    trangle = list(map(int,input().split()))
    if trangle == [0, 0, 0] :
        break
    long_side = max(trangle)
    trangle.pop(trangle.index(long_side))
    if (long_side) ** 2 == (trangle[0]) ** 2 + (trangle[1]) ** 2 :
        output.append('right')
    else :
        output.append('wrong')

for i in range(len(output)) :
    print(output[i])