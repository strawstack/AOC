lo = 156218
hi = 652527

def same(n):
    last = ""
    for c in n:
        if c == last:
            return True
        last = c
    return False

def nondec(n):
    last = 0
    for c in n:
        v = int(c)
        if v < last:
            return False
        last = v
    return True

def sol():
    count = 0
    for n in range(156218, 652527):
        snum = str(n)
        if same(snum) and nondec(snum):
            count += 1
    return count


ans = sol()
print(ans)
