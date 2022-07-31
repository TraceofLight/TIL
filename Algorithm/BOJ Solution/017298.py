# 처음에 서치한 오큰수 및 idx, 그 당시 i 및 수치 기록
# idx 증가 후 수치보다 작을 때 새로 다시 서치 후 오큰수 및 idx 기록, 없을 시 기존 오큰수 출력

import sys

number = int(input())
number_list = list(map(int,sys.stdin.readline().split()))
output = []
start_number = []
big_number = []
for i in range(number) :
    output.append(number_list[i])
    if len(start_number) == 0 :
        start_number.append(i)
    elif start_number[-1] > number_list[i] :
        pass

'''
output = [-1]
bigNumber = [number_list[-1]]

for i in range(number - 2, -1, -1) :
    if number_list[i] < bigNumber[-1] :
        output.append(bigNumber[-1])
        bigNumber.append(number_list[i])
    elif number_list[i] >= bigNumber[-1] :
        if len(bigNumber) >= 2 :
            while number_list[i] >= bigNumber[-1] :
                bigNumber.pop(-1)
                if len(bigNumber) == 1 :
                    break
            if len(bigNumber) == 1 :
                if number_list[i] < bigNumber[0] :
                    output.append(bigNumber[0])
                else :
                    output.append(-1)
                    bigNumber.append(number_list[i])
            else :
                output.append(bigNumber[-1])
        else :
            output.append(-1)
            bigNumber.append(number_list[i])
    else : 
        bigNumber.append(number_list[i])
        output.append(-1)

print(*reversed(output))

top = [0]
low = [0]
counter = 1
new_counter = 1
checker = True
for i in range(number - 1) :
    if counter > 1 :
        if number_list[i] < low[-1] :
            counter = 1
            while number_list[i + new_counter] > number_list[i] :
                if i + counter == number - 2 :
                    output.append(top[-1])
                    checker = False
                    break
                counter += 1
            top.append(number_list[i + counter])
            low.append(number_list[i])
        counter -= 1
        output.append(top[-1]) 
        continue
    elif counter == 1 and i != 0 and top[-1] != 0 :
        top.pop(-1)
    else :
        while number_list[i + counter] <= number_list[i] and checker != False :
            if i + counter == number - 2 :
                output.append(-1)
                checker = False
                break
            counter += 1
        if checker != False :
            top.append(number_list[i + counter])
            low.append(number_list[i])
            output.append(top[-1])
        checker = True

output.append(-1)

print(*output)

# 넣으면서 가장 컸던 순간과 인덱스 기억 

import sys

number = int(input())
number_list = list(map(int,sys.stdin.readline().split()))
output = []
lock_number = 0
lock_index = 0

for i in range(number) :
    # 마지막 숫자는 항상 -1 반환
    if i == number - 1 :
        output.append(-1)
        break
    # lock 가는 과정에서 조금 더 낮은 오큰수를 만났을 때
    elif i < lock_index :
        if i > start_index and number_list[i] < start_number :
            for j in range(i + 1, lock_index) :
                # 만족하는 숫자가 나타났을 경우
                if number_list[i] < number_list[j] :
                    output.append(number_list[j])
                    start_number = number_list[i]
                    start_index = i
                    lock_number = number_list[j]
                    lock_index = j
                    break
                # 끝까지 갔는데 만족하는 숫자가 없을 때
                if j == lock_index - 1 and number_list[i] >= number_list[j] :
                    output.append(lock_number)
                    break
        else :
            output.append(lock_number)
            continue
    # 지금 숫자보다 크면서 오른쪽 수들 중에서 가장 왼쪽에 있는 수 체크
    else :
        for j in range(i + 1, number) :
            # 만족하는 숫자가 나타났을 경우
            if number_list[i] < number_list[j] :
                output.append(number_list[j])
                start_number = number_list[i]
                start_index = i
                lock_number = number_list[j]
                lock_index = j
                break
            # 끝까지 갔는데 만족하는 숫자가 없을 때
            if j == number - 1 and number_list[i] >= number_list[j] :
                output.append(-1)
                break

print(*output)
'''