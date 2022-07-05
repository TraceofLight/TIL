trigger = 0
counter = 0
output = 999
first_number = int(input())
calc = first_number
while trigger == 0 :
    counter = counter + 1
    calc_10 = calc // 10 
    calc_1 = calc % 10
    output = calc_10 + calc_1
    calc = output % 10 + calc_1 * 10
    if first_number == calc :
        break
print(counter)