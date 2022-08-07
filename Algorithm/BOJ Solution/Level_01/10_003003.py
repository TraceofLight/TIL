chess = [1, 1, 2, 2, 2, 8]

piece_list = list(map(int,input().split()))

for i in range(len(chess)) :
    print(chess[i] - piece_list[i], end = ' ')