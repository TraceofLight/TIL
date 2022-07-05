counter = 0
sum_list = []
while counter != 1:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0 :
        counter = 1
    sum_list.append(a + b)
for j in range(len(sum_list)-1) :
    print(sum_list[j])