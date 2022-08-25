import sys
from heapq import *

testcase = int(sys.stdin.readline())
output = []

for each_case in range(testcase):
    length = 0
    order_number = int(sys.stdin.readline().strip('\n'))
    priority_que_high = []
    priority_que_low = []
    del_heap_high = []
    del_heap_low = []
    for _ in range(order_number):
        order_type, target = sys.stdin.readline().strip('\n').split()
        target = int(target)
        if order_type == 'I':
            length += 1
            heappush(priority_que_high, -target)
            heappush(priority_que_low, target)
        elif order_type == 'D':
            if not length:
                continue
            elif target == 1:
                heappush(del_heap_high, heappop(priority_que_high))
                length -= 1
            elif target == -1:
                heappush(del_heap_low, -heappop(priority_que_low))
                length -= 1
    if not length:
        output.append([])
    else:
        while priority_que_high and del_heap_low and priority_que_high[0] == -del_heap_low[0]:
            heappop(priority_que_high)
            heappop(del_heap_low)
        while priority_que_low and del_heap_high and priority_que_low[0] == -del_heap_high[0]:
            heappop(priority_que_low)
            heappop(del_heap_high)
        output.append([-priority_que_high[0], priority_que_low[0]])
for result in output:
    if not result:
        print('EMPTY')
    else:
        print(*result)

'''
def heap_append(heap_list, val): # 최소 힙
    heap_list.append(val)
    cursor = len(heap_list)
    while cursor > 1:
        if heap_list[cursor - 1] < heap_list[cursor // 2 - 1]:
            heap_list[cursor - 1], heap_list[cursor // 2 - 1] = heap_list[cursor // 2 - 1], heap_list[cursor - 1]
            cursor = cursor // 2
        else:
            break
    return heap_list

def heap_sort(heap_list:deque):
    new_list = deque([])
    new_list.append(heap_list.popleft())
    length = len(heap_list)
    while heap_list:
        if length == 1:
            new_list.append(heap_list.popleft())
            break
        else:
            heap_list.appendleft(heap_list.pop())
            cursor = 1
            while True:
                if cursor * 2 + 1 <= length:
                    if heap_list[cursor * 2] <= heap_list[cursor * 2 - 1]:
                        if heap_list[cursor * 2] <= heap_list[cursor - 1]:
                            heap_list[cursor - 1], heap_list[cursor * 2] = heap_list[cursor * 2], heap_list[cursor - 1]
                            cursor = cursor * 2 + 1
                        else:
                            break
                    else:
                        if heap_list[cursor * 2 - 1] <= heap_list[cursor - 1]:
                            heap_list[cursor - 1], heap_list[cursor * 2 - 1] = heap_list[cursor * 2 - 1], heap_list[cursor - 1]
                            cursor = cursor * 2
                        else:
                            break
                elif cursor * 2 <= length:
                    if heap_list[cursor * 2 - 1] <= heap_list[cursor - 1]:
                        heap_list[cursor - 1], heap_list[cursor * 2 - 1] = heap_list[cursor * 2 - 1], heap_list[cursor - 1]
                        cursor = cursor * 2
                    else:
                        break
                else:
                    break
            new_list.append(heap_list.popleft())
            length -= 1
    return new_list
'''

