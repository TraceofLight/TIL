line_count = int(input())
for i in range(line_count) :
    counter = 0
    while counter < line_count - i - 1:
        counter = counter + 1
        print(' ', end='')
    for j in range(i+1) :
        print('*', end='')
    print('')