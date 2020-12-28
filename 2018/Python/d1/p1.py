def sol():
    data = [x.strip() for x in open("d1.txt").readlines()]

    total = 0
    for d in data:
        total += int(d)
    return total

# main
ans = sol()
print(ans)
