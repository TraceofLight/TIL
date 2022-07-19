import numbers


testCase = int(input())
output = []
for i in range(testCase) :
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    x_ = x1 - x2
    y_ = y1 - y2
    find_spot = ((x_/y_)((r2**2-r1**2)/(2*y_)-y1)+x1)**2 - (1 + (x_**2)/(y_**2))(x1**2+y1**2-r1**2)
    if x1 == x2 and y1 == y2 and r1 == r2 :
        output.append(-1)
    elif find_spot > 0 :
        output.append(2)
    elif find_spot == 0 :
        output.append(1)
    elif find_spot < 0 :
        output.append(0)


