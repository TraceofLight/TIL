count_number = int(input())
sum_list = []
a_memory = []
b_memory = []
for i in range(count_number) :
    a, b = input().split()
    a = int(a)
    b = int(b)
    a_memory.append(a)
    b_memory.append(b)
    sum_list.append(a + b)
for j in range(count_number) :
    print("Case #",j+1,": ",a_memory[j]," + ",b_memory[j]," = " ,sum_list[j], sep='')