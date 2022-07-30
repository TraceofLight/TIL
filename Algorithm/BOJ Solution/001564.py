inputFactorialNumber = int(input())
output = 1

for i in range(1, inputFactorialNumber + 1) :
    output *= i
    output = int(str(output).rstrip('0'))
    output %= 1000000000000

if len(str(output)) >= 5 : 
    print(str(output)[-5 :])

else : 
    print(('00000' + str(output))[-5 :])

'''
자릿수를 여분으로 보장하는 이유

2^8 에 5^8 같은 수를 곱했을 때 한 번에 뒷 자리에 0이 8개 생기면서
5자리 이상이 생길 여지가 있기 때문에 여분의 자릿수 보장이 필요하다.
'''