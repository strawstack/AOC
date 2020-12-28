import sys

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def sol():
    # pos=<-6188447,38493894,-4050550>, r=65495976
    data = [x.strip() for x in open("d23.txt").readlines()]

    largest = 0
    loc = None
    bot = []
    for row in data:
        pos, r = row.split(", ")
        r = int(r.split("=")[1])
        pos = pos.split("<")[1]
        pos = [int(x) for x in pos[:-1].split(",")]

        bot.append( [pos, r] )

        if r > largest:
            largest = r
            loc = pos

    total = 0
    for b in bot:

        if dist(b[0], loc) <= largest:
            total += 1
    print(pos)
    return total

# main
ans = sol()
print(ans)
# sys.stdout.flush()
