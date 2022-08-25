import sys
from heapq import *

order_number = int(sys.stdin.readline().rstrip('\n'))
list_plus = []
list_minus = []
length = 0
output = []

for _ in range(order_number):
    order = int(sys.stdin.readline().rstrip('\n'))
    if order == 0:
        if not length:
            output.append(0)
        else:
            if list_plus and list_minus:
                if list_plus[0] >= list_minus[0]:
                    output.append(-heappop(list_minus))
                    length -= 1
                else:
                    output.append(heappop(list_plus))
                    length -= 1
            elif list_plus:
                output.append(heappop(list_plus))
                length -= 1
            elif list_minus:
                output.append(-heappop(list_minus))
                length -= 1
    else:
        if order > 0:
            heappush(list_plus, order)
            length += 1
        else:
            heappush(list_minus, -order)
            length += 1

print(*output, sep='\n')