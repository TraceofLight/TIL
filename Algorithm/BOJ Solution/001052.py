n, k = list(map(int,input().split()))
bottle = []
counter = 0
need_bottle = 0
checker = False

n_raw = bin(n)
bottle = list(n_raw.lstrip('0b'))
length = len(bottle)

for i in range(length) :
    bottle[i] = int(bottle[i]) * (2 ** ((length - 1) - i))

try :
    while True :
        bottle.remove(0)
except :
    pass

length_bottle = len(bottle)
now_bottle = len(bottle)

while True :
    if k == 0 :
        checker = True
        print(-1)
        break
    while now_bottle > k and length_bottle != 0 :
        add_bottle = bottle.pop()
        need_bottle += add_bottle
        bottle.append(2 * add_bottle)
        if length_bottle < 2 :
            continue
        while bottle[-1] == bottle[-2] :
            bottle.pop()
            bottle.append(2 * bottle.pop())
            length_bottle -= 1
            now_bottle -= 1
            if length_bottle < 2 :
                break
        if now_bottle <= k :
            break
    if now_bottle <= k :
        break

if checker == False :
    print(need_bottle)