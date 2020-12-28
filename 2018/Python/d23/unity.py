import sys

X = 0
Y = 1
Z = 2
R = 3

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

    out = open("unity.txt", 'w')
    scale = 1000
    for bot in bots:
        xx = str(bot[X] / scale)
        yy = str(bot[Y] / scale)
        zz = str(bot[Z] / scale)
        rr = str(bot[R] / scale)
        out.write( xx + "," + yy + "," + zz + "," + rr + "\n")



# main
_ = sol()
