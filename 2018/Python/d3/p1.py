def hash(x, y):
    return str(x) + ":" + str(y)

def sol():
    data = [x.strip() for x in open("d3.txt").readlines()]

    map = {}

    for row in data:
        # #1 @ 916,616: 21x29
        n, at, coord, size = row.split(" ")

        x, y = [int(z) for z in coord[:-1].split(",")]
        w, h = [int(z) for z in size.split("x")]

        for i in range(x, x + w):
            for j in range(y, y + h):
                has = hash(i, j)
                if not has in map: map[has] = 0
                map[has] += 1

    count = 0
    for item in map:
        if map[item] > 1:
            count += 1

    # 349428
    # 324947
    #
    return count

# main
ans = sol()
print(ans)
