import sys

card_amount = int(input())
card_info = list(map(int,sys.stdin.readline().split()))
target_amount = int(input())
target_info = list(map(int,sys.stdin.readline().split()))

raw_data = sorted(list(enumerate(target_info)), key = lambda x : x[1])
target_dict = {element[1] : element[0] for element in raw_data}
output = [0 for i in range(target_amount)]

for supply in card_info :
    findOnDict = target_dict.get(supply)
    if findOnDict != None :
        output[findOnDict] += 1

for target in target_info :
    print(output[target_dict[target]], end = ' ')

'''
def binarySearch(val, list, start, end) :
    if start == end :
        if val == list[start] :
            return start
        else :
            return False
    else :
        mid = end - start // 2 
        if val > list[start + mid] :
            return binarySearch(val, list, start + mid + 1, end)
        elif val < list[start + mid] :
            return binarySearch(val, list, start, start + mid - 1)
        elif val == list[start + mid] :
            return start + mid
        elif val != list[start + mid] :
            return False
'''