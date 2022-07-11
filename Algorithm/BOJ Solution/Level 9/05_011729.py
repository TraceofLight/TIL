def hanoi(a) :
    if a == 1 :
        return 1
    if a != 1 :
        t = 2 * hanoi(a - 1) + 1
        return t

def move() :
    return
    
x = int(input())
print(hanoi(x))
