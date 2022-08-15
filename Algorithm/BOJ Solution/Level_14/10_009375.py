import sys

testcase = int(sys.stdin.readline())
output = []

for case in range(testcase):
    total_wear = int(sys.stdin.readline())
    wear_type_list_ = []
    wear_name_list = []
    for _ in range(total_wear):
        wear_name, wear_type = sys.stdin.readline().split()
        wear_type_list_.append(wear_type)
        wear_name_list.append([wear_type, wear_name])
    wear_type_list = [[element] for element in list(set(wear_type_list_))]
    for wear in wear_name_list:
        for wear_type in wear_type_list:
            if wear[0] == wear_type[0]:
                wear_type.append(wear[1])
    result = 1
    for idx in range(len(wear_type_list)):
        result *= len(wear_type_list[idx])
    output.append(result - 1)

print(*output, sep='\n')
