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
trigger = 0
counter = 0
while trigger == 0 :
    print(list_number[counter], end = ' ')
    counter = counter + 1
    if counter == len(list_number) :
        trigger = 1
