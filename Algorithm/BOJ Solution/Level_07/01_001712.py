input = input().split()
a = int(input[0])
b = int(input[1])
c = int(input[2])
while True :
    try :
        bep = a // (c - b) + 1
        if c < b :
            bep = -1
    except :
        bep = -1
    break
print(bep)