cut_pipe = input()
output = 0
stack = []
counter = 0

# 얹을 때 스택에 추가, 자르면 현 스택만큼 카운트
# 괄호 닫을 때 파이프 끝나므로 1카운트씩 추가

for i in range(len(cut_pipe)) :
    if counter >= 1 : # 레이저 괄호 닫은 부분 패스
        counter -= 1
        continue

    if cut_pipe[i] == '(' :
        stack.append(1)
        if cut_pipe[i + 1] == ')' : # 레이저일 경우
            stack.pop()
            output += len(stack)
            counter += 1

    else : # 레이저가 아닌 닫는 괄호일 경우
        stack.pop()
        output += 1

print(output)

'''
# 레이저 따로 분류

for i in range(cut_pipe.stack('')) :
    cut_pipe = cut_pipe.replace('()', '#')

# 얹을 때 스택에 추가, 자르면 현 스택만큼 카운트
# 괄호 닫을 때 파이프 끝나므로 1카운트씩 추가

for i in range(len(cut_pipe)) :
    if cut_pipe[i] == '(' :
        stack +=1
    elif cut_pipe[i] == ')' :
        stack -= 1
        output += 1
    elif cut_pipe[i] == '#' :
        output += stack
'''

