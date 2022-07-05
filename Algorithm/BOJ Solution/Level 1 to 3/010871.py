n, x = input().split()
n = int(n)
x = int(x)
list_element = input().split()
list_number=[]
if int(len(list_element)) > n :
        exit()
for i in range(len(list_element)) :
    if int(list_element[i]) < x :
        list_number.append(list_element[i])
for j in range(len(list_number)) :
    print(list_number[j], end=' ')