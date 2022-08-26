import sys
from heapq import *
from collections import defaultdict

testcase = int(sys.stdin.readline())
output = []

for each_case in range(testcase):
    length = 0
    order_number = int(sys.stdin.readline().strip('\n'))
    del_heap = defaultdict(int)
    priority_que_high = []
    priority_que_low = []
    for _ in range(order_number):
        order_type, target = sys.stdin.readline().strip('\n').split()
        target = int(target)
        if order_type == 'I':
            length += 1
            heappush(priority_que_high, -target)
            heappush(priority_que_low, target)
            del_heap[target] += 1
        elif order_type == 'D':
            if not length:
                continue
            # 중간 제거할 때도 허수를 걸러야 한다!
            elif target == 1:
                while priority_que_high:
                    pop_this = heappop(priority_que_high)
                    if del_heap[-pop_this] != 0:
                        length -= 1
                        del_heap[-pop_this] -= 1
                        break
            elif target == -1:
                while priority_que_low:
                    pop_this = heappop(priority_que_low)
                    if del_heap[pop_this] != 0:
                        length -= 1
                        del_heap[pop_this] -= 1
                        break
    if not length:
        output.append([])
    else:
        while priority_que_high and del_heap[-priority_que_high[0]] == 0:
            heappop(priority_que_high)
        while priority_que_low and del_heap[priority_que_low[0]] == 0:
            heappop(priority_que_low)
        output.append([-priority_que_high[0], priority_que_low[0]])
for result in output:
    if not result:
        print('EMPTY')
    else:
        print(*result)
