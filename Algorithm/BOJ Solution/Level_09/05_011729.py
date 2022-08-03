def hanoi(a) :
    if a == 1 :
        return 1
    if a != 1 :
        t = 2 * hanoi(a - 1) + 1
        return t

def hanoi_go(a, start, middle, goal) :
    if a == 1 :
        print(start, goal)
    else :
        hanoi_go(a - 1, start, goal, middle)
        print(start, goal)
        hanoi_go(a - 1, middle, start, goal)

testNumber = int(input())
print(hanoi(testNumber))
hanoi_go(testNumber, 1, 2, 3)