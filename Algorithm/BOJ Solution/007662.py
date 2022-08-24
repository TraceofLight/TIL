import sys
from heapq import *

testcase = int(sys.stdin.readline())
output = []

for each_case in range(testcase):
    length = 0
    order_number = int(sys.stdin.readline())
    priority_que_high = []
    priority_que_low = []
    del_list = []
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
            if length == 1:
                priority_que_high.clear()
                priority_que_low.clear()
                length -= 0
            elif target == 1:
                heappush(del_list,-heappop(priority_que_high))
                length -= 1
            elif target == -1:
                heappush(del_list,heappop(priority_que_low))
                length -= 1
    if not length:
        output.append([])
    else:
        while -priority_que_high[0] in del_list:
            heappop(priority_que_high)
        while priority_que_low[0] in del_list:
            heappop(priority_que_low)
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
