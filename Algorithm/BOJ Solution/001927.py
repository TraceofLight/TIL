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
        else:
            get_pop = min_heap[0]
            pop_list.append(get_pop)
            min_heap[0] = min_heap[-1]
            min_heap.pop()
            last_idx = len(min_heap)
            cursor = 1
            while True:
                if 2 * cursor < last_idx:
                    if min_heap[2 * cursor - 1] <= min_heap[2 * cursor]:
                        if min_heap[cursor - 1] > min_heap[2 * cursor - 1]:
                            min_heap[cursor - 1], min_heap[2 * cursor - 1] = min_heap[2 * cursor - 1], min_heap[cursor - 1]
                            cursor = 2 * cursor
                            continue
                        else:
                            break
                    else:
                        if min_heap[cursor - 1] > min_heap[2 * cursor]:
                            min_heap[cursor - 1], min_heap[2 * cursor] = min_heap[2 * cursor], min_heap[cursor - 1]
                            cursor = 2 * cursor + 1
                            continue
                        else:
                            break
                elif 2 * cursor - 1 < last_idx:
                    if min_heap[cursor - 1] > min_heap[2 * cursor - 1]:
                        min_heap[cursor - 1], min_heap[2 * cursor - 1] = min_heap[2 * cursor - 1], min_heap[cursor - 1]
                        cursor = 2 * cursor
                        continue
                    else:
                        break
                else:
                    break
    else:
        min_heap.append(input_order)
        cursor = len(min_heap)
        while cursor > 1:
            if min_heap[cursor - 1] < min_heap[cursor // 2 - 1]:
                min_heap[cursor - 1], min_heap[cursor // 2 - 1] = min_heap[cursor // 2 - 1], min_heap[cursor - 1]
                cursor = cursor // 2
            else:
                cursor = cursor // 2

print(*pop_list, sep='\n')