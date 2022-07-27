number = int(input())
number_list = []
for i in range(number) :
    number_list.append(input())
new_list = [int(i) for i in number_list]
new_list.sort()

for i in range(len(new_list)) :
    print(new_list[i])

""" 병렬정렬 시도
new_list = [[int(i)] for i in number_list]

while len(new_list) != 1 :
    length = len(new_list)
    sort = []
    for i in range(length // 2) :
        left = new_list[2*i]
        right = new_list[2*i+1]
        new_element = []
        while len(left) != 0 and len(right) != 0 :
            if left[0] > right[0] :
                new_element.append(right[0])
                right.pop(0)
            elif left[-1] < right[-1] :
                new_element.append(left[0])
                left.pop(0)
            if len(left) == 0 :
                new_element.extend(right)
            if len(right) == 0 :
                new_element.extend(left)
        sort.append(new_element)
    if length % 2 != 0 :
        sort.append(new_list[-1])
    new_list = sort
output = new_list[0]
print(output)
"""