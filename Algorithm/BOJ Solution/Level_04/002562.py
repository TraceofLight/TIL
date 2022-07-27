list_number = []
for i in range(9) :
    list_number.append(input())
list_number = list(map(int,list_number))
print(max(list_number))
print(list_number.index(max(list_number))+1)