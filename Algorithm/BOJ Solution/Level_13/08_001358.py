import sys

width, height, x, y, person = list(map(int, sys.stdin.readline().split()))
radius_link = height / 2
coordinate = []

for _ in range(person):
    coordinate.append(list(map(int, sys.stdin.readline().split())))

count_in_range = 0
for point in coordinate:
    point_x = point[0]
    point_y = point[1]
    if point_x < x:
        if (x - point_x) ** 2 + ((y + radius_link) - point_y) ** 2 <= (radius_link) ** 2:
            count_in_range += 1
    elif x <= point_x and point_x <= x + width:
        if y <= point_y and point_y <= y + height:
            count_in_range += 1
    elif x + width < point_x:
        if ((x + width) - point_x) ** 2 + ((y + radius_link) - point_y) ** 2 <= (radius_link) ** 2:
            count_in_range += 1

print(count_in_range)