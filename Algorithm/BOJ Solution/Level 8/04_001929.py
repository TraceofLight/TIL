decimal = [2, 3, 5, 7]
number = input().split()
m = int(number[0])
n = int(number[1])
p = n ** (1/2)
new_list = list(range(m, n+1))
del_list = [1]
trigger = 0

while True :
    try :
        while decimal[-1] > p :
            last_one = decimal[-1]
            decimal.pop(-1)
            trigger = 1
            if decimal[-1] < p :
                trigger = 2
        if trigger == 2 :
            decimal.append(last_one)
            trigger = 1
        bridge = ((decimal[-1])**2)
        new_number = list(range(decimal[-1] + 1, bridge + 1)) # 소수 확정 범위 ~ 다음 범위로 소수 제한
        for i in range(len(decimal)) : # 소수의 개수만큼 배수 연산
            for j in range(2 , n // decimal[i] + 1) :  # m 에서 n 사이 범위 배수 제한
                del_list.append(decimal[i] * j)
        new_decimal = [i for i in new_number if i not in del_list]
        decimal = decimal + new_decimal
        if trigger == 1 :
            break
    except :
        continue

final_list = [i for i in decimal if i in new_list]
print(*final_list, sep = '\n')
print(len(final_list))