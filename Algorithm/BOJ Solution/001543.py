file = list(input())
word = list(input())
counter = 0
output = 0
checker = 0

for i in range(len(file)) :
    if counter != 0 :
        counter -= 1 # 0 이 아닐 시 스킵 카운터 감소 후 스킵
        continue
    elif file[i] == word[0] :
        for j in range(1, len(word)) :
            checker = 0
            if i + j + 1 > len(file) or file[i + j] != word[j] :
                checker = 1
                break  # 완주 시 checker 가 0
        if checker == 0 : # 해당 단어 길이만큼 스킵
            output += 1
            counter = len(word) - 1

print(output)