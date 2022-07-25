point1 = list(map(int,input().split()))
point2 = list(map(int,input().split()))
point3 = list(map(int,input().split()))
point_list = list(zip(point1, point2, point3))
result = []

for points in point_list :
    for point in points :
        if points.count(point) % 2 :
            result.append(point)

print(*result)