first_number = int(input())
counter = 0
sum = 1
while True :
    counter = counter + 1
    sum = sum + (counter * 6)
    if first_number <= sum :
        break
if first_number == 1 :
    print(1)
else :
    print(counter + 1)