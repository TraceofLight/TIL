def sum_number(a, b) :
    x = int(a[b])
    list_x = list(str(x))
    list_x_ = [int(i) for i in list_x]
    output = sum(list_x_)
    return(output)

input_1 = int(input())
if input_1 == 1 :
    print(0)
else :
    first_input = input_1
    length = len(list(str(input_1)))
    output = []
    if input_1 >= 20 :
        minimum = list(range(input_1 - 9 * length, input_1 + 1))
        minimum_ = [int(i) for i in minimum]
        for i in range(len(minimum_)) :
            if input_1 == minimum_[i] + sum_number(minimum_, i) :
                output.append(minimum_[i])
        if len(output) == 0 :
            print(0)
        else : 
            print(min(output))
    elif input_1 < 20 :
        to_20 = range(1,21)
        for i in range(len(to_20)) :
            if input_1 == to_20[i] + sum_number(to_20, i) :
                output.append(to_20[i])
        if len(output) == 0 :
            print(0)
        else :
            print(min(output))
    else :
        print(0)