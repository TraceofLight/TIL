import sys


def check_condition(target_list, check_list):
    if len(target_list) == len(check_list) + 1:
        is_satisfy = True
        for idx in range(len(check_list)):
            if check_list[idx] == '>':
                if target_list[idx] < target_list[idx + 1]:
                    is_satisfy = False
                    break
            else:
                if target_list[idx] > target_list[idx + 1]:
                    is_satisfy = False
                    break
        if is_satisfy:
            return True
        else:
            return False


def permutation(list, selection, first_selection):
    output = []
    if selection == 0:
        return [[]]
    for idx in range(len(list)):
        element = list[idx]
        for other in permutation(list[:idx] + list[idx + 1:], selection - 1, first_selection):
            check_this = [element] + other
            if len(check_this) != first_selection:
                output.append(check_this)
            else:
                if check_condition(check_this, condition):
                    return check_this
    return output


number_list = list(range(10))
number_list_rev = list(range(9, -1 , -1))
number = int(sys.stdin.readline())
condition = list(sys.stdin.readline().strip().split())[: number + 1]
length_condition = len(condition)
min_val = permutation(number_list, length_condition + 1, length_condition + 1)
max_val = permutation(number_list_rev, length_condition + 1, length_condition + 1)

print(''.join([str(element) for element in max_val]))
print(''.join([str(element) for element in min_val]))
