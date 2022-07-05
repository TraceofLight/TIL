counter = 1
a, b = input().split()
a = int(a)
b = int(b)
while counter != 0 :
    try :
        print(a+b)
        a, b = input().split()
        a = int(a)
        b = int(b)
    except :
        break