import sys

X = 0
Y = 1
Z = 2
R = 3

D = True

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def sol():
    # pos=<-6188447,38493894,-4050550>, r=65495976
    data = [x.strip() for x in open("d23.txt").readlines()]

    bots = [] # list of all bot locations
    for row in data:
        pos, rad = row.split(", ")
        rad = int(rad.split("=")[1])
        pos = pos.split("<")[1]
        x, y, z = [int(x) for x in pos[:-1].split(",")]
        bots.append( [x, y, z, rad] )

    # original: 37.61759, 92.35812, -2.916725, 62.68641
    guess = [37617588,92358114,-2916725,62686405]

    # DFS outward from this loc
    # find the cheapest value that
    # still has the same intersections





# main
ans = sol()
print(ans)
# sys.stdout.flush()
# 3000 wrong
# 89843475 wrong
# 70000000 wrong
# 68443957 wrong
# 82650984 wrong
# 68443942 wrong
