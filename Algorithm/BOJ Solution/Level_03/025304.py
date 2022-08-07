total = int(input())
goods_number = int(input())
ans = 0

for i in range(goods_number):
    price, amount = list(map(int,input().split()))
    ans += price * amount

if total == ans :
    print('Yes')
else :
    print('No')