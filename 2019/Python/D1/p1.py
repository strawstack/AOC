lines = [x[:-1] for x in open("input.txt").readlines()]

def sol():
    ans = 0
    for x in lines:
        ans += int(x)//3 - 2
    return ans
ans = sol()
print(ans)
