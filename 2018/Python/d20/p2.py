import sys

ROW = 0
COL = 1

def hash(r, c):
    return (r, c)

def search(loc, grid, moves, offset):

    dir = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1)
    }

    i = offset
    while i < len(moves):

        item = moves[i]
        r, c = loc

        if item == "|": return True, i
        if item == ")": return False, i

        if item in ["N", "E", "S", "W"]:
            nr = r + dir[item][ROW]
            nc = c + dir[item][COL]

            h1 = hash(r, c)
            h2 = hash(nr, nc)
            if not h1 in grid: grid[h1] = []
            if not h2 in grid: grid[h2] = []

            grid[h1].append( h2 )
            grid[h2].append( h1 )

            loc = (nr, nc)

        if item == "(":
            bar = True
            while bar:
                bar, index = search(loc, grid, moves, i+1)
                i = index

        i += 1

def bfs(loc, grid):

    visited = {}
    q = [(loc, 0)]
    hi = 0

    far_rooms = {}

    while len(q) != 0:
        cur, dist = q.pop(0)
        visited[cur] = True
        hi = max(hi, dist)

        if dist >= 1000:
            if not cur in far_rooms:
                far_rooms[cur] = True

        for child in grid[cur]:
            if not child in visited:
                q.append( (child, dist + 1) )

    return len(far_rooms)

def sol():

    data = open("d20.txt").read().strip()

    grid = {}
    _ = search((0, 0), grid, data, 0)

    hi = bfs((0,0), grid)
    return hi

# main
ans = sol()
print(ans)
# sys.stdout.flush()
