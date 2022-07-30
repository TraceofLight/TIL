import sys

number_get = int(input())
list_number = list(map(int,sys.stdin.readline().split()))
number_check = int(input())
list_check = sorted(list(map(int,sys.stdin.readline().split())))

def binarySearch(value, a) :
    length = len(a)
    if length == 1 :
        if a[0] == value :
            return 1
        else :
            return 0
    elif length == 0 :
            pass
    elif a[length // 2] == value :
            return 1
    else :
        try :
            binarySearch(value,a[length // 2 -1 :])
            binarySearch(value,a[: length // 2 + 1])
        except :
            pass

output = []

for number in list_check :
    output.append(binarySearch(number, list_number))

print(*output)