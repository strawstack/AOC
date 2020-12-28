import sys

X = 0
Y = 1
N = 2

D = False

data = [x.strip() for x in open("d6.txt").readlines()]
coords = []

def man(i, j, x, y):
    return abs(i-x) + abs(j-y)

def closest(nx):

    dist = []
    all  = []

    for coord in coords:

        x, y, n = coord
        d = man(nx[X], nx[Y], x, y)

        dist.append( (n, d) )
        all.append(d)

    best  = float('inf')
    index = 0

    for n, d in dist:

        if d < best:
            best  = d
            index = n

    if all.count(best) > 1:
        return False

    return index

def hash(x,y):
    return str(x) + "::" + str(y)

def bfs(n):

    visited = {}
    start = coords[n]
    if D: print(" coord:", start)
    q = [start]

    value = 1

    while len(q) != 0:

        cur = q.pop(0)
        myhash = hash(cur[X], cur[Y])
        visited[myhash] = True

        if D: print(" pop:", cur)

        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for off in offsets:

            child = (cur[X] + off[X], cur[Y] + off[Y], cur[N])

            myhash = hash(child[X], child[Y])
            if myhash in visited: continue
            visited[myhash] = True

            res = closest(child)

            if res == child[N]:

                value += 1
                if value == 10000: return value
                q.append(child)

    return value

def sol():

    # BFS from each point until its exhausted

    for i, item in enumerate(data):
        x, y = [int(x) for x in item.split(", ")]
        coords.append( (x, y, i) )

    values = []
    for i in range(len(coords)):
        if D: print("BFS:", i)
        value = bfs(i)
        values.append(value)

    # 399
    # 400
    # 3568
    #
    values = filter(lambda x: x != 10000, values)
    return max(values)

# main
ans = sol()
print(ans)
