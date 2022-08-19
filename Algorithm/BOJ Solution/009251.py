import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

string1_cursor = 0
string2_cursor = 0

string_sameness = 0
counter = 0
length1 = len(string1)

while string1_cursor != length1:
    print(string1_cursor)
    if counter > 0:
        counter -= 1
        string1_cursor += 1
        continue
    if string1_cursor + counter <= length1 - 1:
        while string1[string1_cursor + counter] == string2[counter]:
            counter += 1
            if string_sameness < counter:
                string_sameness = counter
        string1_cursor += 1
    else:
        continue

print(string_sameness)
