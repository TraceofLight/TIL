import sys

sensor_number = int(sys.stdin.readline())
central = int(sys.stdin.readline())

sensor_list = sorted(list(map(int, sys.stdin.readline().split())))
distance_list_raw = []

if sensor_number == 1:
    print(0)
else:
    for idx in range(sensor_number - 1):
        distance_list_raw.append(sensor_list[idx + 1] - sensor_list[idx])
    distance_list = sorted(distance_list_raw)
    for _ in range(central - 1):
        distance_list.pop()
    print(sum(distance_list))