number = int(input())

counter = 0

while number != 1 :
    if number % 3 == 0 :
        number = number // 3
        counter += 1
    elif number % 3 == 1 :
        number = (number - 1) // 3
        counter += 2
    elif number % 3 == 2 :
        number = (number - 2) // 3
        counter += 3
    elif number == 2 :
        number = number // 2
        counter += 1

print(counter)