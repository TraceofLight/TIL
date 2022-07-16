number = int(input())
output = []
for i in range(number) :
    plane = []
    n, word = map(int, input().split())
    for j in range(n) : 
        input_plane_ = input().split()
        input_plane = list([int(i) for i in input_plane_])
        plane.append(input_plane)
    space = []
    # 가로
    for j in range(n) :
        space_ = []
        counter = 0
        for k in range(n - 1) :
            if plane[j][k] == 1 :
                counter = counter + 1
                if k == n - 2 and plane[j][k + 1] == 1 :
                    counter = counter + 1
                    space.append(counter)
                    continue
            if plane[j][k] != plane[j][k+1] :
                space.append(counter)
                counter = 0
    for j in range(n) :
        counter = 0
        for k in range(n - 1) :
            if plane[k][j] == 1 :
                counter = counter + 1
                if k == n - 2 and plane[k+1][j] == 1 :
                    counter = counter + 1
                    space.append(counter)
                    continue
            if plane[k][j] != plane[k+1][j] :
                space.append(counter)
                counter = 0
    result = 0
    for i in range(len(space)) :
        if space[i] == word :
            result += 1
    output.append(result)
for i in range(len(output)) :
    print('#', i + 1, ' ', output[i], sep ='')