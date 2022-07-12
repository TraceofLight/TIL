number = int(input())
counter = 1
six = ['666']
output = [666]
while True :
    if number == 1 :
        break
    six.insert(0, '0')
    number_list = []
    for i in range(len(six)) :
        a = six[-1]
        six.pop()
        six.insert(0, a)
        b = ''.join(six)
        number_list.append(b)
    for i in range(len(number_list)) :
        print(number_list)
    if len(output) >= number :
        break
    """
    for i in range(len(six)) :
        if i == len(six) :
            print('a')
        six[i] = 6
        six[i + 1] = 0
    for j in range(10) :
        six[i] = j
        merge = map(str, ''.join(six))
        output.append(merge)
        counter = counter + 1
        if counter == number :
            trigger = 1
        six.insert(0, '#')
    break
    """
print(six(-1))