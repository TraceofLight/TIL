import sys
import math
formula = sys.stdin.readline().strip()
stack1 = []

formula = formula.replace('-', '*-')
formula = formula.replace('+', '*')

formula = list(formula.split('*'))
new_list = []

for chr in formula:
    if chr.isnumeric():
        new_list.append(int(chr))
    else:
        new_list.append(chr)
print(new_list)