input = int(input())
counter = 2
if input == 1 :
    exit()
first_input = input
while counter <= first_input :
    if input % counter == 0 :
        print(counter)
        input = input / counter
    else :
        counter = counter + 1