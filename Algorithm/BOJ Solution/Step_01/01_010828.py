import sys
ord_number = int(input())
stack1 = []

for i in range(ord_number) :
    input_process = sys.stdin.readline()
    input_process = input_process.split('\n')[0]
    if input_process.startswith('push') :
        stack1.append(int(input_process.split('push ')[1]))
    elif input_process == 'pop' :
        try : 
            print(stack1.pop(-1))
        except :
            print(-1)
    elif input_process == 'size' :
        print(len(stack1))
    elif input_process == 'empty' :
        if len(stack1) != 0 :
            print(0)
        else :
            print(1)
    elif input_process == 'top' :
        try :
            print(stack1[-1])
        except :
            print(-1)
