lines = [x[:-1] for x in open("input.txt").readlines()]

def fuel(x):
    f = x//3 - 2
    if f <= 0:
        return 0
    else:
        return f + fuel(f)

def sol():
    ans = 0
    for x in lines:
        ans += fuel(int(x))
    return ans
    
ans = sol()
print(ans)
