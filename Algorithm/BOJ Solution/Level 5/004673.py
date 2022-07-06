def selfnumber(a) :
    sum_number = 0
    not_selfnumber = []
    for i in range(1, a+1) :
        sum_number = i
        sep_number = list(str(i))
        while sum_number <= a :
            for j in range(len(sep_number)) : #생성된 숫자 더하기
                sum_number = sum_number + int(sep_number[j])
            sep_number = list(str(sum_number))
            if sum_number not in not_selfnumber and (sum_number <= a) : # 셀프 넘버가 아닌 리스트 추가 과정
                not_selfnumber.append(sum_number)
    self_number = []
    for k in range(1, a+1) :
        self_number.append(k)
    self_number = [x for x in self_number if x not in not_selfnumber]
    for l in range(len(self_number)) :
        print(self_number[l])

selfnumber(10000)