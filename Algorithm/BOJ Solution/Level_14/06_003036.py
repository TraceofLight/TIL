import sys

ring_number = int(sys.stdin.readline())
ring_list = list(map(int, sys.stdin.readline().split()))

for idx in range(ring_number):
    if idx == 0:
        continue
    first_ring = ring_list[0]
    counter = 2
    while (first_ring != 1 and ring_list[idx] != 1 and 
        counter <= first_ring and counter <= ring_list[idx]):
        while not first_ring % counter and not ring_list[idx] % counter:
            first_ring = first_ring // counter
            ring_list[idx] = ring_list[idx] // counter
        counter += 1
    print(f'{first_ring}/{ring_list[idx]}')