import sys

card_number = int(sys.stdin.readline())
cardset_price = list(map(int, sys.stdin.readline().split()))
card_types = len(cardset_price)
val_list = [0]

def buy_card(val):
    global val_list
    global card_types
    global cardset_price
    length = len(val_list)
    if val <= length:
        return val_list[val]
    else:
        if val <= card_types:
            if length == 1:
                val_list.append(cardset_price[0])
                length += 1
            for _ in range(length, val + 1):
                cost_list = []
                for idx in range(length):
                    cost_list.append(cardset_price[idx] + val_list[length - idx - 1])
                val_list.append(min(cost_list))
                length += 1
            return val_list[val]
        else:
            for _ in range(length, card_types):
                cost_list = []
                for idx in range(length):
                    cost_list.append(val_list[length - idx - 1] + cardset_price[idx])
                val_list.append(min(cost_list))
                length += 1
            for idx in range(card_types, val + 1):
                repeat_counter = idx // card_types
                left_counter = idx - (repeat_counter * card_types)
                val_list.append(repeat_counter * val_list[card_types - 1] + val_list[left_counter - 1])
                length += 1
            return val_list[val]

print(buy_card(card_number))