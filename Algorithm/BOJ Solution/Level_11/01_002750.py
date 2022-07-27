# 버블 정렬

number = int(input())
number_list = []
for i in range(number) :
    number_list.append(input())
new_list = [int(i) for i in number_list]
counter = 0

while counter != len(new_list) - 1 :
    for i in range(len(new_list) - 1) :
        a = new_list[i]
        b = new_list[i + 1]
        if a > b :
            new_list[i] = b
            new_list[i + 1] = a
    counter = counter + 1

print(*new_list, sep = '\n')