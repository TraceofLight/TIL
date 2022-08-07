def factorial(a) :
    if a <= 1 :
        return 1
    result = a * factorial(a-1)
    return result

x = int(input())
print(factorial(x))