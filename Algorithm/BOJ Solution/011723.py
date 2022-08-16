import sys

set1 = set()

operation_number = int(sys.stdin.readline())

for _ in range(operation_number):
    order = sys.stdin.readline().strip()
    if order.startswith('add'):
        order = order.lstrip('add ')
        set1.add(int(order))
    elif order.startswith('remove'):
        order = order.lstrip('remove ')
        set1.discard(int(order))
    elif order.startswith('check'):
        order = order.lstrip('check ')
        if int(order) in set1:
            print(1)
        else:
            print(0) 
    elif order.startswith('toggle'):
        order = order.lstrip('toggle ')
        if int(order) in set1:
            set1.discard(int(order))
        else:
            set1.add(int(order)) 
    elif order.startswith('all'):
        set1 = {num for num in range(1, 21)}
    elif order.startswith('empty'):
        set1.clear()