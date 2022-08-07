a, b = list(map(int,input().split()))

while a != 0 and b != 0 :
    if a > b :
        a = a % b
    else :
        b = b % a

common_multiple = max(a, b)

for i in range(common_multiple) :
    print(1, end ='')

# 유클리드 호제법
# 최대공약수를 찾는 방법으로 
# 어느 한 쪽이 0이 될 때까지 큰 수를 작은 수로 나눈 나머지를 구하고 
# 이를 반복하여 한 쪽이 0이 될 경우 나머지 한 쪽이 최대공약수이다.