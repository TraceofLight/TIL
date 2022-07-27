testcase = int(input()) #케이스 개수
output = [] #출력값 보관
for i in range(testcase) : #케이스 횟수만큼 반복
    chunk = input().split()
    rpt_number = int(chunk[0])
    chunk.pop(0)
    element = list(chunk[0])
    new_word = []
    for j in range(len(element)) : # 문자 주입 반복
        for k in range(rpt_number) : # 문자 횟수 반복
            new_word.append(element[j])
    new_word = ''.join(new_word)
    output.append(new_word)
for l in range(len(output)) :
    print(output[l])

#alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'
#alphanumeric_ = list(alphanumeric)
#    for k in range(len(new_word)) : # alphanumeric 조건 미달 배제
#        if (new_word[k]) not in alphanumeric_ :
#            exit()