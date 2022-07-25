import copy

melon = int(input())
coordinate = [0, 0]
coord_list = []

# 방향에 따른 좌표 이동

def move(direction, length) : 
    global coordinate
    global cood_list
    if direction == 1 :
        coordinate[0] += length
    elif direction == 2 :
        coordinate[0] -= length
    elif direction == 3 :
        coordinate[1] -= length
    elif direction == 4 :
        coordinate[1] += length

# 각 좌표 구하기

for i in range(6) : 
    direction, length = list(map(int, input().split()))
    move(direction, length)
    coord_list.append(copy.deepcopy(coordinate))

# 좌표 분리
range = list(zip(coord_list[0], coord_list[1], coord_list[2], coord_list[3], coord_list[4], coord_list[5]))

# 변의 길이 체크
x_range = sorted(list(set(range[0])))
y_range = sorted(list(set(range[1])))

# 큰 사각형에서 빠진 점 체크
spot_list = list(zip(x_range, y_range))
spot_list = [list(i) for i in spot_list]
find_one = [spot for spot in spot_list if spot not in coord_list]

# 넓이 연산
big_square = (max(x_range) - min(x_range)) * (max(y_range) - min(y_range))

if len(find_one) >= 1 :
    small_square = (abs(find_one[0][0] - x_range[1])) * (abs(find_one[0][1] - y_range[1]))
else :
    small_square = 0

print((big_square - small_square) * melon)