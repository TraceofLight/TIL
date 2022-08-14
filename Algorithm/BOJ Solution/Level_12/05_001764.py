import sys

n, m = list(map(int, sys.stdin.readline().split()))
set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(sys.stdin.readline().strip())

for _ in range(m):
    set_m.add(sys.stdin.readline().strip())

set_m_and_n = set_n & set_m

list_m_and_n = sorted(list(set_m_and_n))

print(len(list_m_and_n))
for element in list_m_and_n:
    print(element)
