def distance(a, b, c, d) :
    a, b, c, d = int(a), int(b), int(c), int(d)
    result = ((c - a) ** 2) + ((d - b)** 2)
    return int(result)

testCase = int(input())
planet_info = []
satisfy_option = 0
output = []
for i in range(testCase) :
    x1, y1, x2, y2 = map(int,input().split())
    orbit_number = int(input())
    for j in range(orbit_number) :
        planet_info.append(list(map(int,input().split())))
    counter = 0
    for j in range(orbit_number) :
        cx = planet_info[j][0]
        cy = planet_info[j][1]
        cr = planet_info[j][2]
        if distance(x1, y1, cx, cy) < cr**2 :
            counter += 1
        if distance(x2, y2, cx, cy) < cr**2 :
            counter += 1
        if distance(x1, y1, cx, cy) < cr**2 and distance(x2, y2, cx, cy) < cr**2 :
            counter += -2
        satisfy_option += counter
        counter = 0
    output.append(satisfy_option)
    satisfy_option = 0
    planet_info = []

for i in range(testCase) :
    print(output[i])