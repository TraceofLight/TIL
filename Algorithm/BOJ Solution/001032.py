number = int(input())

# 첫 단어 받기
first_fileName = list(input())

# 다음 단어부터 비교
for i in range(number - 1) :
    fileName = list(input())
    for j in range(len(fileName)) :
        # 이미 ? 일 때
        if first_fileName[j] == '?' :
            continue
        # 아니면 검수
        elif fileName[j] != first_fileName[j] :
            first_fileName[j] = '?'

print(''.join(first_fileName))