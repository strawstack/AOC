def sol():
    data = [x.strip() for x in open("d1.txt").readlines()]

    sam = {}
    total = 0
    sam[total] = True

    while True:
        for d in data:
            x = int(d)

            total += x

            if total in sam:
                return total

            sam[total] = True

# main
ans = sol()
print(ans)
