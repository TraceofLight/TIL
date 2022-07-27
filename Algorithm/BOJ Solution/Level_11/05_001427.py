input_list = list(input())
number = [i for i in input_list]
number.sort()
a = number.reverse()
output = int(''.join(number))
print(output)