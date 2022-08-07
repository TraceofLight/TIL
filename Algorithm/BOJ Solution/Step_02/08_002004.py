def factorial_0(a) :

    if a == 0 :
        return 0, 0

    multiple_5 = 0
    multiple_2 = 0

    calc = a
    while True :
        calc = calc // 2
        multiple_2 += calc
        if calc == 0 :
            break
    calc = a
    while True :
        calc = calc // 5
        multiple_5 += calc
        if calc == 0 :
            break

    return multiple_2, multiple_5

n, m = list(map(int,input().split()))

result = min(factorial_0(n)[0] - factorial_0(m)[0] - factorial_0(n - m)[0], factorial_0(n)[1] - factorial_0(m)[1] - factorial_0(n - m)[1])

if result > 0 or result < 0 :
    print(result)

else :
    print(0)

'''
def combination_0(a, b) :
    if a == 0 and b == 0:
        return 0

    multiple_5 = 0
    multiple_2 = 0
    counter = 1

    while True :
        checker = counter
        while not checker % 2 :
            checker = checker // 2
            multiple_2 += 1
        while not checker % 5 :
            checker = checker // 5
            multiple_5 += 1
        if counter == b :
            multiple_b = [multiple_2, multiple_5]
        if counter == a :
            break
        counter += 1
    
    result = min(multiple_2 - 2 * multiple_b[0], multiple_5 - 2 * multiple_b[1])

    if result > 0 :
        return result
    else :
        return 0

n, m = list(map(int,input().split()))

print(combination_0(n, m))
'''