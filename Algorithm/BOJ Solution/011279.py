import sys
from collections import deque

order_number = int(sys.stdin.readline())
max_hip = deque([])
pop_list = []
length = 0

for _ in range(order_number):
    order = int(sys.stdin.readline())
    if not order:
        if not max_hip:
            pop_list.append(0)
        else:
            pop_this = max_hip[0]
            max_hip[0] = max_hip[length - 1]
            pop_list.append(pop_this)
            max_hip.pop()
            length -= 1
            cursor = 1
            while True:
                if cursor * 2 + 1 <= length:
                    if max_hip[cursor * 2] >= max_hip[cursor * 2 - 1]:
                        if max_hip[cursor * 2] > max_hip[cursor - 1]:
                            max_hip[cursor - 1], max_hip[cursor * 2] = max_hip[cursor * 2], max_hip[cursor - 1]
                            cursor = cursor * 2 + 1
                        else:
                            break
                    else:
                        if max_hip[cursor * 2 - 1] > max_hip[cursor - 1]:
                            max_hip[cursor - 1], max_hip[cursor * 2 - 1] = max_hip[cursor * 2 - 1], max_hip[cursor - 1]
                            cursor = cursor * 2
                        else:
                            break
                elif cursor * 2 <= length:
                    if max_hip[cursor * 2 - 1] > max_hip[cursor - 1]:
                        max_hip[cursor - 1], max_hip[cursor * 2 - 1] = max_hip[cursor * 2 - 1], max_hip[cursor - 1]
                        cursor = cursor * 2
                    else:
                        break
                else:
                    break
    else:
        max_hip.append(order)
        length += 1
        cursor = length
        while cursor > 1:
            if max_hip[cursor - 1] > max_hip[cursor // 2 - 1]:
                max_hip[cursor - 1], max_hip[cursor // 2 - 1] = max_hip[cursor // 2 - 1], max_hip[cursor - 1]
                cursor = cursor // 2
            else:
                break

print(*pop_list, sep='\n')
