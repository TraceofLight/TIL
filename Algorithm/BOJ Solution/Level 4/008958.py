def sum(n) : # 1 ~ n까지 덧셈연산
    a = 0
    for i in range(n) :
        a = a + (i + 1)
    return a

quiz_frequency = int(input())
quiz = []
scoreboard = []
for i in range(quiz_frequency) : #퀴즈 항목 반복 수 받아와서 알파벳 단위 분해 
    quiz.append(input())
    quiz_split = list(quiz[i])
    counter = 0
    score = 0
    length = 0
    for j in range(len(quiz_split)) : #i번째 스트링 내 점수 합산 (스트링 길이만큼 반복)
        if quiz_split[j] == 'O' :
            length = length + 1
        elif quiz_split[j] != 'O' :
            score = score + sum(length)
            length = 0
        if j == len(quiz_split) - 1 :
            score = score + sum(length)
            length = 0
    scoreboard.append(score)
for k in range(quiz_frequency) :
    print(scoreboard[k])