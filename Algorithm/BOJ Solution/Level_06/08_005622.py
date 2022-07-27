# 기존 알파벳 to ASCII 재활용
word = input()
word_element = list(word)
output = []
element_index = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)
word_ascii = [ord(i) for i in word_element]
for j in range(len(word_ascii)) : # 알파벳 맞춰 코드 정리
    if word_ascii[j] > 90 :
        word_ascii[j] = word_ascii[j] - 97
    else :
        word_ascii[j] = word_ascii[j] - 65
    number = int(word_ascii[j]) + 1
    element_index.append(number)

# 다이얼 변환 후 시간 계산
time = 0
dial_number = []
for i in range(len(element_index)) :
    if element_index[i] <= 3 :
        dial_number.append(2)
    elif element_index[i] <= 6 :
        dial_number.append(3)
    elif element_index[i] <= 9 :
        dial_number.append(4)
    elif element_index[i] <= 12 :
        dial_number.append(5)
    elif element_index[i] <= 15 :
        dial_number.append(6)
    elif element_index[i] <= 19 :
        dial_number.append(7)
    elif element_index[i] <= 22 :
        dial_number.append(8)
    else :
        dial_number.append(9)
for k in range(len(dial_number)) :
    time = time + dial_number[k] + 1
print(time)