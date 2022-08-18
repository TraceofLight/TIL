import sys
import math
testcase = int(sys.stdin.readline())
output = []

for case_each in range(testcase):
    get_value = False
    m, n, target_m, target_n = map(int, sys.stdin.readline().split())
    if m == n:
        if target_m <= m and target_n <= n and m == n and target_m == target_n:
            output.append(m)
        else:
            output.append(-1)
    else:
        input_m, input_n, f_target_m, f_target_n = m, n, target_m, target_n
        max_number = math.lcm(m, n)
        gcd_number = math.gcd(m, n)
        m //= gcd_number
        n //= gcd_number
        lcm_number = math.lcm(m, n)
        target_m %= m
        target_n %= n
        mod_m = lcm_number // m
        mod_n = lcm_number // n
        '''
        counter1 = 1
        while (counter1 * mod_m) % m != 1:
            print(counter1)
            counter1 += 1
        counter2 = 1
        while (counter2 * mod_n) % n != 1:
            print(counter2)
            counter2 += 1
        '''
        counter1 = (m - 1) * abs((mod_m % m) - m)
        counter2 = (n - 1) * abs((mod_n % n) - n)
        result = ((target_m * mod_m * (counter1)) +
                    (target_n * mod_n * (counter2)))
        result = result % lcm_number
        print(result)
        while result <= max_number:
            if result % input_m == f_target_m and result % input_n == f_target_n:
                output.append(int(result))
                get_value = True
                break
            else:
                result += lcm_number
        if get_value == False:
            output.append(-1)
            continue

print(*output, sep = '\n')

'''
import sys
import math
testcase = int(sys.stdin.readline())
output = []

for case_each in range(testcase):
    get_value = False
    m, n, target_m, target_n = map(int, sys.stdin.readline().split())
    max_number = math.lcm(m, n)
    for idx_m in range(max_number // m):
        for idx_n in range(max_number // n):
            if m * idx_m + target_m == n * idx_n + target_n:
                output.append(m * idx_m + target_m)
                get_value = True
            if get_value:
                break
        if get_value:
            break
    if not get_value:
        output.append(-1)

print(*output, sep = '\n')
'''