import sys
from collections import deque

testcase = int(sys.stdin.readline())
output = []

def heap_sort(heap_list, value: None):
    if value != None:
        heap_list.append(value)
    last_idx = len(heap_list)
    cursor = last_idx
    while cursor > 1:
        if heap_list[cursor - 1] < heap_list[cursor // 2 - 1]:
            heap_list[cursor - 1], heap_list[cursor // 2 - 1] = heap_list[cursor // 2 - 1], heap_list[cursor - 1]
        else:
            break
    return heap_list

for each_case in range(testcase):
    order_number = int(sys.stdin.readline())
    priority_que = deque([])
    length = 0
    for _ in range(order_number):
        order_type, target = sys.stdin.readline().strip('\n').split()
        target = int(target)
        if order_type == 'I':
            if not priority_que:
                priority_que.append(target)
            else:
                heap_sort(priority_que, target)
        elif order_type == 'D':
            if not priority_que:
                continue
            elif target == 1:
                priority_que.pop()
            elif target == -1:
                priority_que.popleft()
    if not priority_que:
        output.append([])
    else:
        output.append([priority_que[-1], priority_que[0]])

for result in output:
    if not result:
        print('EMPTY')
    else:
        print(*result)
