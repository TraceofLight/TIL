number = int(input())
list_ = []

for i in range(number) :
    line = int(input())
    list_.append([])
    for j in range(line) :
        letter = input().split()
        letter[1] = int(letter[1])
        list_[i].append(letter)

for i in range(len(list_)) :
    print('#', i + 1, sep = '')
    output = []
    for j in range(len(list_[i])) :
        output.append(list_[i][j][0] * list_[i][j][1])
    output_ = list(''.join(output))

    for i in range(len(output_) // 10 + 1) :
        if i == len(output_) // 10 + 1 :
            print(*output_[i * 10 : len(output_)], sep = '')
            continue
        print(*output_[i * 10 : i * 10 + 10], sep = '')
