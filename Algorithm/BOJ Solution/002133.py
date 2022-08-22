import sys

fill_tile = [[1, 2, 0], [3, 6, 2]]

input_number = int(sys.stdin.readline())

if input_number % 2:
    print(0)

else:
    input_number = input_number // 2
    length = len(fill_tile)
    if input_number <= length:
        print(sum(fill_tile[input_number - 1]))
    else:
        for idx in range(length, input_number):
            fill_tile.append([sum(fill_tile[idx - 1]), sum(fill_tile[idx - 1]) * 2, fill_tile[idx - 1][1] + fill_tile[idx - 1][2]])
        print(sum(fill_tile[input_number - 1]))