from tokenize import group


def hanoi_result(a) :
    if a == 1 :
        return 1
    else :
        t = 2 * hanoi_result(a - 1) + 1
        return t

def build(a) :
    
    start = 1
    sub = 2
    goal = 3
    while a != 0 :
        if a == 1 :
            print(start, goal, sep = '')
            break
        elif a == 2 :
            print(start, sub)
            print(start, goal)
            print(sub, goal)
            break
        elif a % 2 == 0 :
            sub = 2
            goal = 3
            print(start, sub, sep = '')
            print(start, goal, sep = '')
            print(sub, goal)



x = int(input())
print(hanoi_result(x))
build(x)

