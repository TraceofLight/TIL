x, y = list(map(int,input().split()))
common_number = 1
not_common_number = 1
counter = 2

while True :
    if x == 1 or y == 1:
        break
    elif y % counter == 0 :
        if x % counter == 0 :
            common_number *= counter
            x /= counter
            y /= counter
        else :
            not_common_number *= counter
            y /= counter
    else :
        counter += 1

if x >= y :
    print(common_number)
    print(int(common_number * not_common_number * x))

else :
    print(common_number)
    print(int(common_number * not_common_number * y))
