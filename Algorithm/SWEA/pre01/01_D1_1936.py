a = input().split()
b = [int(i) for i in a]

if b[0] == 3 and b[1] == 1 :
    print('B')
elif b[0] == 1 and b[1] == 3 :
    print('A')
elif b[0] > b[1] :
    print('A')
elif b[0] < b[1] :
    print('B')