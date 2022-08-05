n, k = list(map(int,input().split()))
cup = []
counter = 0
need_cup = 0
checker = False

while n > 0 :
    if n >= 2 ** counter and n < 2 ** (counter + 1) :
        cup.append(counter)
        n = n - 2 ** counter
        counter = 0
    else :
        counter += 1

now_cup = len(cup)

while now_cup > k :
    if now_cup > 0 :
        low_number = cup.pop()
        need_cup += 2 ** (low_number)
        cup.append(low_number + 1)
        if len(cup) > 2 :
            new_counter = 1
            while cup[-1] == cup[-2] :
                cup.pop()
                cup.append(cup.pop() + 1)
                now_cup -= 1
                if now_cup < 2 :
                    break
        if now_cup <= 0 and now_cup :
            print(-1)
            checker = True
            break
    else :
        print(-1)
        checker = True
        break

if checker == False :
    print(need_cup)