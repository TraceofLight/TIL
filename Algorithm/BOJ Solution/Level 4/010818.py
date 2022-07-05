n = int(input())
list_number = input().split()
if len(list_number) != n :
    exit()
list_number = list(map(int,list_number))
max_number = max(list_number)
min_number = min(list_number)
print(min_number, max_number)