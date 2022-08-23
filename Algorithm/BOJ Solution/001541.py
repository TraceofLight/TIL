import sys

formula_raw = sys.stdin.readline().strip()
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

result = 0
is_minus = False
for value in formula:
    if value < 0:
        is_minus = True
        result += value
        continue
    else:
        if is_minus:
            result -= value
        else:
            result += value

print(result)