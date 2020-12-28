import sys

X = 0
Y = 1
N = 2

D = False

data = [x.strip() for x in open("d6.txt").readlines()]
coords = []

def man(i, j, x, y):
    return abs(i-x) + abs(j-y)

# if max is less than 10000
def closest(nx):

    total = 0

    for coord in coords:

        x, y, n = coord
        m = man(nx[X], nx[Y], x, y)
        total += m

    return total < 10000

def hash(x,y):
    return str(x) + "::" + str(y)

def bfs(n):

    visited = {}
    start = coords[n]
    if D: print(" coord:", start)
    q = [start]
    myhash = hash(start[X], start[Y])
    visited[myhash] = True
    value = 1

    while len(q) != 0:

        cur = q.pop(0)

        if D: print(" pop:", cur)

        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for off in offsets:

            child = (cur[X] + off[X], cur[Y] + off[Y], cur[N])

            myhash = hash(child[X], child[Y])
            if myhash in visited: continue

            res = closest(child)

            if res:
                value += 1
                q.append(child)
                visited[myhash] = True


    return value

def sol():

    # BFS from each point until its exhausted

    for i, item in enumerate(data):
        x, y = [int(x) for x in item.split(", ")]
        coords.append( (x, y, i) )

    value = bfs(0)
    return value

# main
# 48978 too high
# 48977 too low
ans = sol()
print(ans)
