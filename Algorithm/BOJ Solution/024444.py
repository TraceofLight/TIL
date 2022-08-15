import sys
from collections import deque

nodes, lines, start_point = list(map(int, sys.stdin.readline().split()))
line_list = []
node_list = [set() for _ in range(nodes)]
visited = []

progress_que = deque([])

