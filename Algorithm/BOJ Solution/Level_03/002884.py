a, b = input().split()
a = int(a)
b = int(b)
if b >= 45 :
    b = b - 45
else :
    b = b + 15
    a = a - 1
if a < 0 :
    a = 23
print (a, b)