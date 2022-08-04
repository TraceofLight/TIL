n, k = list(map(int,input().split()))
cup_count = 0
cup = 0
cup_stats = []
while k > cup :
    if n == 0 and cup_count <= k:
        print(cup)
        break
    else :
        counter = 0
        while n > 2**counter :
            counter += 1
            cup_count += 1
        n = n - 2**(counter - 1)
if cup_count > k :
    n += 1
    cup += 1