def Fibonacci(a) :
    if a == 0 :
        return 0
    elif a == 1 :
        return 1
    result = Fibonacci(a - 1) + Fibonacci(a - 2)
    return(result)

x = int(input())
print(Fibonacci(x))