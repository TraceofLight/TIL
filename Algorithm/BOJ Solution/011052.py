import sys

pack_amount = int(sys.stdin.readline())
pack_list = list(map(int, sys.stdin.readline().split()))
pack_type = len(pack_list)
pack_price = sorted([[pack_list[idx] / (idx + 1), idx + 1] for idx in range(len(pack_list))],key=lambda x : x[0])
val_list = []


def buy_card(val):
    global val_list
    global pack_price
    length = len(val_list)
    if val <= length:
        result = 0
        for count_info in val_list[val - 1]:
            result += count_info[0] * count_info[1]
        return result
    else:
        for idx in range(length, val):
            add_list = val_list[idx // pack_type - 1]
            remainder = idx % pack_type
            append_list = [[add_list[idx] + val_list[idx][0], idx + 1] for idx in range(pack_type)]

            
print(pack_price)