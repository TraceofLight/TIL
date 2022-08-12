import sys

number = int(sys.stdin.readline())
ans_list = [0, 1, 1, 1]


def downto1(val):
    global ans_list
    if len(ans_list) >= val:
        return ans_list[val]
    else:
        for idx in range(len(ans_list), val + 1):
            if idx % 3 == 0 and idx % 2 == 0:
                ans_list.append(min(downto1(idx - 1), downto1(idx // 2), downto1(idx // 3)) + 1)
            elif idx % 3 == 0:
                ans_list.append(min(downto1(idx - 1), downto1(idx // 3)) + 1)
            elif idx % 2 == 0:
                ans_list.append(min(downto1(idx - 1), downto1(idx // 2)) + 1)
            else:
                ans_list.append(ans_list[idx - 1] + 1)
        return ans_list[val]


if number == 1:
    print(0)
else:
    print(downto1(number))