def distance(a, b, c, d) :
    result = ((c - a) ** 2 + (d - b)** 2) ** (1 / 2)
    return int(result)

testCase = int(input())
planet_info_ = []
planet_info = []
satisfy_option = 0
output = []
for i in range(testCase) :
    x1, y1, x2, y2 = map(int,input().split())
    print(x1)
    orbit_number = int(input())
    for j in range(orbit_number) :
        planet_info_ = list(map(int,input().split()))
        planet_info.append(planet_info_)
    print(planet_info)
    for j in range(orbit_number) :
        if distance(x1, y1, planet_info[j][0], planet_info[j][1]) < planet_info[j][2] :
            satisfy_option += 1
        if distance(x2, y2, planet_info[j][0], planet_info[j][1]) < planet_info[j][2] :
            satisfy_option += 1
        if distance(x1, y1, planet_info[j][0], planet_info[j][1]) < planet_info[j][2] and distance(x2, y2, planet_info[j][0], planet_info[j][1]) < planet_info[j][2] :
            satisfy_option -= 2
    output.append(satisfy_option)
    satisfy_option = 0

for i in range(testCase) :
    print(output[i])