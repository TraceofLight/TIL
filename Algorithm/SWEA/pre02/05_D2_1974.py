number = int(input())
output = []
perfect_list = [i for i in range(1, 10)]
plane_og = []
plane_ = []
checker = 1

for i in range(9 * number) : 
    inputplane = input().split()
    input_plane = list([int(i) for i in inputplane])
    plane_.append(input_plane)

for i in range(number) :
    plane_og.append(plane_[9 * i : 9 * i + 9])

for i in range(number) :
    plane = plane_og[i]
    oneToNine1 = []
    oneToNine2 = []
    for j in range(9) :
        for k in range(9) :
            oneToNine1.append(plane[j][k])
            oneToNine2.append(plane[k][j])
        a = oneToNine1.sort()
        a_ = oneToNine2.sort()
        if oneToNine1 != perfect_list or oneToNine2 != perfect_list :
            checker = 0
        oneToNine1 = []
        oneToNine2 = []
    oneToNine3 = []
    for j in range(0, 9, 3) :
        for k in range(0, 9, 3) :
            for l in range(3) :
                for m in range(3) :
                    oneToNine3.append(plane[j+l][k+m])
            b = oneToNine3.sort()
            if oneToNine3 != perfect_list :
                checker = 0
            oneToNine3 = []
    output.append(checker)
    checker = 1
    plane = []
for i in range(len(output)) :
    print('#', i + 1, ' ', output[i], sep = '')