import copy

n, k = list(map(int,input().split()))
values = []
for i in range(n) :
    values.append(int(input()))

counter = 0
cost = 0
calc_k = copy.deepcopy(k)
length = len(values)

for i in range(length) :
    if cost >= k :
        break
    else :
        coin = values[length - i - 1]
        coin_number = calc_k // coin
        if coin_number > 0 :
            calc_k = calc_k - coin_number * coin
            cost += coin_number * coin
            counter = counter + coin_number

print(counter)
