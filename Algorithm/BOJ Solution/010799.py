cut_pipe = input()
output = 0
count = 0

# 얹을 때 스택에 추가, 자르면 현 스택만큼 카운트
# 괄호 닫을 때 파이프 끝나므로 1카운트씩 추가

for i in range(len(cut_pipe)) :
    if cut_pipe[i] == '(' :
        count += 1
    elif cut_pipe[i] == ')' :
        if cut_pipe[i - 1] == '(': # 레이저 파츠
            count -= 1
            output += count
        else :
            count -= 1
            output += 1

print(output)

'''
# 레이저 따로 분류

for i in range(cut_pipe.count('')) :
    cut_pipe = cut_pipe.replace('()', '#')

# 얹을 때 스택에 추가, 자르면 현 스택만큼 카운트
# 괄호 닫을 때 파이프 끝나므로 1카운트씩 추가

for i in range(len(cut_pipe)) :
    if cut_pipe[i] == '(' :
        count +=1
    elif cut_pipe[i] == ')' :
        count -= 1
        output += 1
    elif cut_pipe[i] == '#' :
        output += count
'''

