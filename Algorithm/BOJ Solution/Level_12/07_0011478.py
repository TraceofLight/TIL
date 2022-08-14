import sys

string_input = sys.stdin.readline().strip()

length = len(string_input)
group_string = []

for start_index in range(length):
    for end_index in range(start_index + 1, length + 1):
        group_string.append(string_input[start_index : end_index])

set_string = set(group_string)

print(len(set_string))
