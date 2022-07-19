number = int(input())
output_list = []
output = []
for i in range(number) :
    plane = []
    n = int(input())
    for j in range(n) : 
        inputplane = list(input())
        input_plane = list([int(i) for i in inputplane])
        plane.append(input_plane)
    output.append(plane)
print(output)