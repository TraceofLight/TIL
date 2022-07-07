cycle = int(input())
output = 0
for i in range(cycle) :
    word = input()
    input_word = word
    # 들어가는 문자 갯수 세기
    element_number = set(word)
    element_number = list(element_number)
    number = len(element_number)
    # 첫 문자 잡기
    list_word = list(input_word)
    letter = list_word[0]
    # 변하는 횟수 체크
    counter = 0
    for i in range(len(list_word)) :
        if letter != list_word[i] :
            letter = list_word[i]
            counter = counter + 1
    if counter == number - 1 :
        output = output + 1
print(output)