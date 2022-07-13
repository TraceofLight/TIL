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
        number_element = list(number_list[i])
        number_element = [int(i) for i in number_element]
        number_element.reverse()
        for j in range(number_element.count(0)) :
            while True :
                if number_element.index(0) == None :
                    break
                for k in range(9) :
                    new_element = number_element
                    new_element[number_element.index(0)] = k
                    new_output = ''.join(new_element)
                    output.append(new_output)
                new_element[number_element.index(0)] = 'a'
        print(number_element)
    if len(output) >= number :
        break
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
print(six[-1])