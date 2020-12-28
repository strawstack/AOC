# n = 6548
import sys

def power(x, y):
    rackID = x + 10
    begin = rackID * y
    after = begin + 6548
    after *= rackID
    if after < 100:
        after = 0
    else:
        after //= 100
        after = after % 10
    return after - 5

def cell_power(x, y, size):
    pow = 0
    for i in range(size):
        for j in range(size):
            pow += power(x + i, y + j)
    return pow

def sol():
    #data = [x.strip() for x in open("d11.txt").readlines()]

    best_power = 0
    best_coord = (1, 1)

    size = 3

    best_power = 0
    best_coord = (1, 1)
    for r in range(300 - (size - 1)):
        for c in range(300 - (size - 1)):
            nx = cell_power(r, c, size)
            if nx > best_power:
                best_power = nx
                best_coord = (r, c)

    return best_power, best_coord


# main
power, coord  = sol()
print(power)
print(coord)


# 233,250,12
