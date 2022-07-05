list_element = []
for i in range(3) :
    list_element.append(input())
list_element = list(map(int,list_element))
multiple_element = 1
for j in range(3) :
    multiple_element = multiple_element * list_element[j]
string_num = str(multiple_element)
new_number = []
new_number.extend(string_num)
new_number = list(map(int,new_number))
for k in range(10) :
    print(new_number.count(k))