import sys

k, n = list(map(int,input().split()))

line_list = []

for i in range(k) :
    line_list.append(int(sys.stdin.readline().strip()))

line_list = list(sorted(line_list))

def binarySearch(list, amount, start, end) :
    if start == end :
        result_chop = 0
        for length in list :
            result_chop += length // start
        if result_chop >= amount :
            return end
        else :
            return False
    elif end - start == 1 :
        result_chop = 0
        for i in range(2) :
            for length in list :
                result_chop += length // (end - i)
            if result_chop >= amount :
                return end - i
        return False
    else :
        mid = (end - start) // 2
        result_chop = 0
        for length in list :
            result_chop += length // (end - mid)
        if result_chop < amount :
            return binarySearch(list, amount, start, end - mid - 1)
        elif result_chop > amount :
            return binarySearch(list, amount, end - mid + 1, end)
        elif result_chop == amount :
            return end - mid

result = binarySearch(line_list, n, 1, line_list[-1])
after = result
while True :
    result = binarySearch(line_list, n, after, line_list[-1])
    if result == after :
        break
    after = result

print(result)