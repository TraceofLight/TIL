from distutils.log import error
import math

def root(a) :
    b = (a)**(1/2)
    b = math.ceil(b)
    return b

number = input().split()
m = int(float(number[0]))
n = int(float(number[1]))
checking_root = n
bridge= []
decimal = []
delete_list = []

while checking_root != 2 :
    checking_root = root(checking_root)
    bridge.append(checking_root)
bridge_new = bridge.reverse()
print(bridge)

while True :
        try :
            for i in range(len(bridge)) :
                for j in range(2, (bridge[i + 1] // bridge[i]) + 1) :
                    delete_list.append(bridge[i] * j)
        except :
            for j in range(2, (n // bridge[i]) + 1) :
                delete_list.append(bridge[len(bridge)-1] * j)
            break
print(delete_list)



"""

number = input().split()
m = int(float(number[0]))
n = int(float(number[1]))
p = 0
root_n = n**(1/2)
under_p = []
trigger = 0
delete_list = [1]
list = list(range(m, n + 1))

# 체 사용을 위한 소수 p 선별
for i in reversed(range(math.ceil(root_n))) :
    for j in range(2, i) :
        trigger = 0
        if i % j == 0 :
            trigger = 1
            break
    if trigger == 0 :
        p = i
        break
    trigger = 0

# 소수 골라내기 (p까지)
for k in range(2, p) :
    if k == 1 :
        continue
    for l in range(2, k) :
        if k % l == 0 :
            trigger = 1
            break
    if trigger == 0 :
        under_p.append(k)
    trigger = 0
under_p.append(p)
while True :
    try :
        for a in range(len(under_p)) :
            for b in range(2, (n // under_p[a]) + 1) :
                delete_list.append(under_p[a] * b)
        break
    except :
        continue

new_list = [i for i in list if i not in delete_list]

for z in range(len(new_list)) :
    print(new_list[z])

number = input().split()
m = int(number[0])
n = int(number[1])
trigger = 0
# 소수 골라내기
for i in range(m, n + 1) :
    counter = 1
    if i == 1 :
        continue
    for j in range(2, i) :
        if i % j == 0 :
            trigger = 1
            break
    if trigger == 0 :
        print(i)
    trigger = 0
"""

"""
for i in range(m, n + 1) :
    counter = 1
    if i == 1 :
        continue
    while True :
        counter = counter + 1
        if counter >= i :
            print(i)
            break
        if i % counter == 0 :
            break
"""