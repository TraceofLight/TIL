melon = int(input())
num_dir = []
num_len = []

# input 리스트에 할당
for i in range(6) :
    direction, length = list(map(int,input().split()))
    num_dir.append(direction)
    num_len.append(length)

x_range = [0]
y_range = [0]
coordinate = []

# 좌표 처리
for i in range(6) : 
    if num_dir[i] == 1 :
        x_range.append(x_range[-1] + num_len[i])
    elif num_dir[i] == 2 :
        x_range.append(x_range[-1] - num_len[i])
    elif num_dir[i] == 3 :
        y_range.append(y_range[-1] + num_len[i])
    elif num_dir[i] == 4 :
        y_range.append(y_range[-1] - num_len[i])
    coordinate.append([x_range[-1], y_range[-1]])

# x, y 좌표의 범위 체크
x_range = (sorted(list(set(x_range))))
y_range = (sorted(list(set(y_range))))

x_len = sorted(list(set([abs(i - j) for i in x_range for j in x_range])))
y_len = sorted(list(set([abs(i - j) for i in y_range for j in y_range])))

# 큰 사각형의 빈 귀퉁이 찾기
find_spot = [[i, j] for i in x_range for j in y_range]
spot_ = [element for element in find_spot if element not in coordinate]
spot = [element for element in spot_ if element[0] != x_range[1] if element[1] != y_range[1]]

# 넓이 계산
max_square = x_len[-1] * y_len[-1]
small_square = abs(spot[0][0] - x_range[1]) * abs(spot[0][1] - y_range[1])

print((max_square - small_square) * melon)