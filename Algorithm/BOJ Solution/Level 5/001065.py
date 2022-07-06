number = int(input())
counter = 99
if number >= 1 and number < 100 :
    print(number)
elif number >= 100 and number < 1000 :
    for i in range(100, number + 1) :
        number_1 = list(str(i))
        number_2 = [int(j) for j in number_1]
        if (number_2[0] + number_2[2]) / 2 == number_2[1] :
            counter = counter + 1
    print(counter)
else :
    for k in range(100, 1000) :
        number_1 = list(str(k))
        number_2 = [int(l) for l in number_1]
        if (number_2[0] + number_2[2]) / 2 == number_2[1] :
            counter = counter + 1
    print(counter)