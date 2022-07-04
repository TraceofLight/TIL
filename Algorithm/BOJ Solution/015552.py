count_number = int(input())
sum_list = []
for i in range(count_number) :
    a, b = input().split()
    a = int(a)
    b = int(b)
    sum_list.append(a + b)
for j in range(count_number) :
    print(sum_list[j])