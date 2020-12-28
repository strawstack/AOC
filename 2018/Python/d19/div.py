import math
n = 10551428

total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i

print(total)

# 476 too low
# 10551904 too low
# 18741072
