number = int(input())
output = []
for i in range(number) :
    a = list(input())
    code = 1
    for j in range(len(a)//2) :
        if a[j] != a[-(1+j)] :
            code = 0
            break
    output.append(code)
for i in range(len(output)) :
    print('#', i + 1,' ', output[i], sep ='')