number = int(input())
list_ = input().split()
list_ = [int(i) for i in list_]
output_list = list(range(number))
sign = []
output_sign = [(i - i) for i in range(number)]
counter = 0
for i in range(number) :
    if list_[i] < 0 :
        list_[i] = abs(list_[i]) - 1
        sign.append(-1)
    else :
        list_[i] = list_[i] - 1
        sign.append(1)
print(list_)
print(output_list)
print(sign)
print(output_sign)

while list_ != output_list or sign != output_sign :
    for j in range(number - 1, 0, -1) :
        check1 = list_[j]
        check2 = sign[j]
        if check1 != j :
            start = list_.index(j)
            a = list_[start : j+1]
            b = sign[start : j+1]
            b = [-i for i in b]
            reverse_a = list(reversed(a))
            reverse_b = list(reversed(b))
            print(reverse_a)
            print(reverse_b)
            break
    break
