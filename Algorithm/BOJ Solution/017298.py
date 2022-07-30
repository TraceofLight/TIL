import sys

number = int(input())
number_list = list(map(int,sys.stdin.readline().split()))
output = []
lock_number = number_list[0]
lock_index = 0

for i in range(number) :
    # 마지막 숫자는 항상 -1 반환
    if i == number - 1 :
        output.append(-1)
        break
    # 지금 숫자보다 크면서 오른쪽 수들 중에서 가장 왼쪽에 있는 수 체크
    elif i < lock_index :
        output.append(lock_number)
        continue
    else :
        for j in range(i + 1, number) :
            # 만족하는 숫자가 나타났을 경우
            if number_list[i] < number_list[j] :
                output.append(number_list[j])
                lock_number = number_list[j]
                lock_index = j
                break
            # 끝까지 갔는데 만족하는 숫자가 없을 때
            if j == number - 1 and number_list[i] >= number_list[j] :
                output.append(-1)
                break

print(*output)