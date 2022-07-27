def star(a) :
    a = int(a)
    if a == 3 :
        list_ = [[], [], []]
        for i in range(3):
            for j in range(3) :
                list_[i[j]].append('*')
                if i == 1 and j == 1 : 
                    list_[i[j]].append(' ')
        for i in len(list_) :
            print(list_[i])
        
    else :
        a_width = len(range(a)) 
        for j in range(a) :
            for i in range(a) :
                if a_width * (1/3) < j and a_width * (2/3) >= j and a_width * (1/3) > i and a_width * (2/3) >= i :
                    print('', sep = '', end = '')
                elif i == len(range(a)) - 1 :
                    print('*', sep = '', end = '\n')
                else :
                    star(a/3)

x = int(input())
star(x)