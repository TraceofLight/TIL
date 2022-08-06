def binarySearch(value, a, start, end) : # slicing 대신 좌표 직접 지정
    length = end - start + 1
    if length == 0 :
        return 0
    elif length == 1 :
        if a[start] == value :
            return 1
        else :
            return 0

    length_2 = length // 2 - 1
    target = a[start + length_2]

    if value > target :
        return binarySearch(value, a, start + length_2 + 1, end)
    elif value < target :
        return binarySearch(value, a, start, start + length_2 - 1)
    else :
        return 1

import sys

check_number = int(input())
group_a = sorted(list(map(int,sys.stdin.readline().split())))
numberInAorNot = int(input())
groupInAorNot = list(map(int,sys.stdin.readline().split()))

group_start = group_a[0]
group_end = group_a[-1]

for number in groupInAorNot :
    if number < group_start or number > group_end : # 범위 밖 쳐내기
        print(0)
    else :
        print(binarySearch(number, group_a, 0, check_number - 1))
