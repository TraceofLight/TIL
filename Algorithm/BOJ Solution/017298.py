import sys
from collections import deque

number = int(input())
number_list = list(map(int,sys.stdin.readline().split()))
number_info = deque([])

'''
import sys
from collections import deque

number = int(input())
number_list = list(map(int,sys.stdin.readline().split()))
number_info = deque([])

for i in range(number) :
    checker = True
    if i == number - 1 :
        print(-1)
        break
    try :
        if i == number_info[-1][2] :
            number_info.pop()
        number_info[1]
        if number_list[i] == number_info[-1][1] :
            print(number_info[-1][0], end = ' ')
            continue
        if number_list[i] < number_info[-1][1] :
            counter = 0
            while number_list[i] >= number_list[i + counter] :
                if i + counter == number_info[-1][2] - 1 :
                    print(number_info[-1][0], end = ' ')
                    checker = False
                    break
                counter += 1
            if checker == True :
                print(number_list[i + counter], end = ' ')
                number_info.append([number_list[i + counter], number_list[i], i + counter])
                continue
    except :
        counter = 0
        while number_list[i] >= number_list[i + counter] :
            if i + counter == number - 1:
                print(-1, end = ' ')
                checker = False
                break
            counter += 1
        if checker == True :
            print(number_list[i + counter], end = ' ')
            number_info.append([number_list[i + counter], number_list[i], i + counter])
            continue
'''