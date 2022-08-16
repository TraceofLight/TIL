import sys

counter = 0

def z_function(idx_x, idx_y, n):
    global counter
    if n == 1:
        if idx_x <= 0:
            if idx_y <= 0:
                counter += 0
            else:
                counter += 2
        else:
            if idx_y <= 0:
                counter += 1
            else:
                counter += 3
        return counter
    else:
        if idx_x <= 2 ** (n - 1) - 1:
            if idx_y <= 2 ** (n - 1) - 1:
                counter += ((2 ** (n - 1)) ** 2) * 0
            else:
                counter += ((2 ** (n - 1)) ** 2) * 2
                idx_y -= (2 ** (n - 1))
        else:
            idx_x -= (2 ** (n - 1))
            if idx_y <= 2 ** (n - 1) - 1:
                counter += ((2 ** (n - 1)) ** 2) * 1
            else:
                counter += ((2 ** (n - 1)) ** 2) * 3
                idx_y -= (2 ** (n - 1))
        return z_function(idx_x, idx_y, n - 1)

number, y, x = map(int, sys.stdin.readline().split())

print(z_function(x, y, number))