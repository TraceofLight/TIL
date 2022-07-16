number = int(input())
output = []
for i in range(number) :
    length_a, length_b = map(int,input().split())
    a_= input().split()
    a = [int(i) for i in a_]
    b_ = input().split()
    b = [int(i) for i in b_]
    if length_a > length_b :
        result = []
        for i in range(len(a)-len(b) + 1) :
            sum = 0
            for j in range(len(b)) :
                sum = sum + a[j + i] * b[j]
            result.append(sum)
        output.append(max(result))
    elif length_a < length_b :
        result = []
        for i in range(len(b)-len(a) + 1) :
            sum = 0
            for j in range(len(a)) :
                sum = sum + a[j] * b[j + i]
            result.append(sum)
        output.append(max(result))
    elif length_a == length_b : 
        sum = 0
        for i in range(len(a)) :
            sum = sum + a[i] * b[i]
        output.append(sum)
for i in range(len(output)) :
    print('#', i + 1, ' ', output[i], sep = '')
