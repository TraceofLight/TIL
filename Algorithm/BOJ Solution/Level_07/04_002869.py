input = input().split()
a = int(input[0])
b = int(input[1])
v = int(input[2])
day_first = (v - a) // (a - b) 
if (v - a) % (a - b) != 0 :
    day_first = day_first + 1
day = int(day_first + 1)
print(day)