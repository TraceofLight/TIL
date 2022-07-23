

testCase = int(input()) # 테스트 횟수
output = []
checker = []
for i in range(testCase) :
    number, keyRule = list(map(int,input().split()))
    takeTime = list(map(int,input().split())) # 소요 시간 input
    route = []
    for j in range(keyRule) :
        route.append(list(map(int,input().split()))) # 루트 확보
    goal = int(input())
    
    reverse_route = [goal]
    def destination(a) :
        global reverse_route
        reverse_route.append(a[0])
        if not destination(a[0]) :
            break 
        return destination(a[0])

    # input 정보 초기화
    structure = []
    route = []

for i in range(testCase) :
    print(output[i])
print(checker)