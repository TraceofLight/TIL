element = []
for i in range(10) :
    element.append(input())
element = list(map(int,element))
for j in range(10) :
    element[j] = element[j] % 42
counter = 0
for k in range(42) :
    if element.count(k) != 0 :
        counter = counter + 1
print(counter)