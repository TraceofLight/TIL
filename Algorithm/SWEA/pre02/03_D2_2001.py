number = int(input())
output = []
for i in range(number) :
    plane = []
    n, m = map(int, input().split())
    for j in range(n) : 
        input_plane_ = input().split()
        input_plane = list([int(i) for i in input_plane_])
        plane.append(input_plane)
    output_list = []
    for j in range(n-m + 1) :
        for k in range(n-m + 1)  :
            sum_number = 0
            for l in range(m) :
                for o in range(m) :
                    sum_number += plane[j+l][k + o]
            output_list.append(sum_number)
    output.append(max(output_list))
for i in range(len(output)) :
    print('#', i + 1, ' ', output[i], sep ='')