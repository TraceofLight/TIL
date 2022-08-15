def factorial_0(a) :
    if a == 0 :
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
        if counter == a :
            break
        counter += 1

    return min(multiple_2, multiple_5)

input_number = int(input())

print(factorial_0(input_number))

# 이 문제는 알고리즘 강의 풀이 리스트에도 존재

'''
def factorial(a) :
    if a == 1 :
        return 1
    else :
        return a * factorial(a - 1)

input_number = int(input())

arr = str(factorial(input_number))
length = len(arr)
counter = 0

for i in range(length) :
    if arr[-(i + 1)] == '0' :
        counter += 1
        continue
    else :
        break

print(counter)
'''