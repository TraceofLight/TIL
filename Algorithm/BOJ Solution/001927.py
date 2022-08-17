import sys
from collections import deque

order_number = int(sys.stdin.readline())
pop_list = []
min_heap = deque([])
for order in range(order_number):
    input_order = int(sys.stdin.readline())
    if input_order == 0:
        if len(min_heap) == 0:
            pop_list.append(0)
            print(min_heap)
        else:
            pop_list.append(min_heap.popleft())
            root_node = min_heap[0]
            start_node = root_node
            last_node = min_heap[-1]
            print(min_heap)
    else:
        min_heap.append(input_order)
        cursor = len(min_heap)
        last_idx = cursor
        while cursor > 1:
            cursor //= 2
            if min_heap[cursor - 1] > min_heap[last_idx - 1]:
                min_heap[cursor - 1], min_heap[last_idx - 1] = min_heap[last_idx - 1], min_heap[cursor - 1]
                last_idx = cursor
            else:
                break
        print(min_heap)

print(*pop_list, sep='\n')