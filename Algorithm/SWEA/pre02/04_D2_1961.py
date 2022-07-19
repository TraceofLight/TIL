def str_list(x) :
    result_def = [str(i) for i in x]
    return result_def

number = int(input())
output_list = []
output = []
for i in range(number) :
    output.append([])
    plane = []
    n = int(input())
    for j in range(n) : 
        inputplane = input().split()
        input_plane = list([int(i) for i in inputplane])
        plane.append(input_plane)
    # 90도 회전 (3회 반복)
    for l in range(3) :
        new_layer = []
        for j in range(n) :
            line1 = []
            for k in range(n) :
                line1.append(plane[n - k -  1][j])
            new_layer.append(line1)
        plane = new_layer
        output_list.append(new_layer)
    for j in range(n) :
        a_ = output_list[0][j]
        b_ = output_list[1][j]
        c_ = output_list[2][j]
        a = ''.join(str_list(a_))
        b = ''.join(str_list(b_))
        c = ''.join(str_list(c_))
        d = a + ' ' + b + ' ' + c
        output[-1].append(d)
    output_list = []
for i in range(len(output)) :
        print('#', i + 1, sep = '')
        for j in range(len(output[i])) :
            print(output[i][j])