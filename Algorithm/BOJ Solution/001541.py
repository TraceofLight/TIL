import sys
import math
formula_raw = sys.stdin.readline().strip()
stack1 = []

formula_raw = formula_raw.replace('-', '*-')
formula_raw = formula_raw.replace('+', '*')

formula_raw = list(formula_raw.split('*'))
formula = []

get_minus = []
counter = 0
for chr in formula_raw:
    formula.append(int(chr))
    counter += 1
    if int(chr) < 0:
        get_minus.append(counter)

for idx in range(1):
    pass