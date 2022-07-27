def factorial(a) :
    number = 1
    for i in range(int(a)) :
        number = number * (i + 1)
    return (number)

testcase = int(input())
output = []
for i in range(testcase) :
    floor = int(input()) + 1
    room_number = int(input()) - 1
    result = factorial(floor + room_number) / (factorial(room_number) * factorial(floor))
    output.append(result)
for j in range(len(output)) :
    print(int(output[j]))