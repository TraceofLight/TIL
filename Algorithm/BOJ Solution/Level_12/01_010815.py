import sys

number_get = int(input())
list_number = list(map(int,sys.stdin.readline().split()))
number_check = int(input())
list_check = list(map(int,sys.stdin.readline().split()))
output = [0 for i in range(number_check)]

for i in range(len(list_check)) :
    try :
        list_number.index(list_check[i])
        output[i] = 1
    except :    
        continue

print(*output)