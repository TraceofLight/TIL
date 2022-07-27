x = int(input())
first_x = x
sum_number = 0
while True :
    sum_number = sum_number + 1
    backup = x
    x = x - sum_number
    if x <= 0 :
        break
if sum_number % 2 == 0 : 
    print(backup, '/', sum_number - backup + 1, sep = '')
else :
    print(sum_number - backup + 1, '/', backup, sep = '')