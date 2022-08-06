import sys

number_n = int(input())
list_n = list(map(int,sys.stdin.readline().split()))
number_m = int(input())
list_m = sorted(enumerate(list(map(int,sys.stdin.readline().split()))), key= lambda x : x[1])
list_output = [0 for i in range(number_m)]

def binarySearch(value, number_list, start, end) :
    if start > end :
        return None

    length = end - start + 1

    if length == 1 :
        if value != number_list[start][1] :
            return None
        else :
            return number_list[start][0]

    else :
        target = length // 2
        if number_list[start + target][1] < value :
            return binarySearch(value, number_list, start + target + 1, end)
        elif number_list[start + target][1] > value :
            return binarySearch(value, number_list, start, start + target - 1)
        else :
            return number_list[start + target][0]

for number in list_n :
    try :
        list_output[binarySearch(number, list_m, 0, number_m - 1)] += 1
    except :
        continue

print(*list_output)