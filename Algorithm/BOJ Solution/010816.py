'''
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

import sys

number_n = int(input())
list_n = list(map(int,sys.stdin.readline().split()))
number_m = int(input())
list_m_proto = list(map(int,sys.stdin.readline().split()))
list_m = [[i[1],i[0]] for i in sorted(enumerate(list_m_proto),key=lambda x : x[1])]
dict_m = dict(list_m)
list_output = [0 for i in range(number_m)]

def binarySearch(value, number_list, start, end) :

    if end <= start :
        return None

    length = end - start + 1

    if length == 0 :
        return None

    if length == 1 :
        if value != number_list[start][0] :
            return None
        else :
            return number_list[start][1]

    else :
        mid = length // 2
        if number_list[start + mid][0] < value :
            return binarySearch(value, number_list, start + mid + 1, end)
        elif number_list[start + mid][0] > value :
            return binarySearch(value, number_list, start, start + mid - 1)
        else :
            return number_list[start + mid][1]

for number in list_n :
    try :
        list_output[binarySearch(number, list_m, 0, number_m - 1)] += 1
    except :
        continue

for element in list_m_proto:
    print(list_output[dict_m[element]], end = ' ')

'''
def diffusionchecker(a : list, b : int, c : list) :
    try :
        if a[b][1] == a[b + 1][1] :
            c[b + 1][0] += 1
            diffusionchecker(a, b + 1, c)
        if  a[b][1] == a[b - 1][1] :
            c[b - 1][0] += 1
            diffusionchecker(a, b - 1, c)
    except :
        None
'''