from collections import Counter
import sys

caseNumber = int(input())
case = list(map(int,sys.stdin.readline().split()))
listNumber = int(input())
list_number = list(map(int,sys.stdin.readline().split()))
list_count = [0 for i in range(listNumber)]

list_number.sort()
case.sort()

def binarySearch(a) :
    pass

'''
for i in range(listNumber) :
    print(case.count(list_number[i]), end = ' ')
    try : 
        case.remove(list_number[i])
    except :
        continue


for number in list_number :
    result = Counter(case).get(number)
    if result == None :
        print(0, end = ' ')
    else :
        print(result, end = ' ')
'''