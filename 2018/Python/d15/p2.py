import sys

Z = False

R = 0 # row
C = 1 # col
H = 2 # health
S = 2 # steps
T = 3 # type
D = 4 # isDead

def hash(x):
    return str(x[R]) + "::" + str(x[C])

# return True if unit dies, False otherwise
def damage(nr, nc, units, grid, i):
    for unit in units:
        if unit[R] == nr and unit[C] == nc:
            if unit[T] == "G":
                unit[H] -= i # do damage to unit
            else:
                unit[H] -= 3
            if unit[H] <= 0:
                unit[D] = True # mark unit as dead
                grid[unit[R]][unit[C]] = "." # remove unit from grid
                return True
    return False

def do_damage(possible, nr, nc, units, grid, i):
    c_units = [x[:] for x in units] # copy
    c_units = filter(lambda u: (u[R], u[C]) in possible, c_units)
    c_units = list(sorted(c_units, key=lambda x: x[H]))
    lowest = c_units[0]
    if Z: print("  attacks:", lowest)
    return damage(lowest[R], lowest[C], units, grid, i)

# move unit to given square
def move_unit(unit, m, grid):
    icon = grid[unit[R]][unit[C]]
    grid[unit[R]][unit[C]] = "."
    unit[R] = m[R]
    unit[C] = m[C]
    grid[m[R]][m[C]] = icon

# get best move of the, at most four moves, that
# a unit can make, return False if no move possible
def best_move(unit, grid):
    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)] # up, left, right, down
    best = float("inf")
    m = None
    for move in moves:
        nr = unit[R] + move[R]
        nc = unit[C] + move[C]

        if grid[nr][nc] == ".":

            start = (nr, nc, 1, unit[T])
            cost = bfs(start, grid)
            if cost < best:
                best = cost
                m = (nr, nc)

    if best == float("inf"):
        return False

    return m # best move

# shortest path each direction from start to end
def bfs(start, grid):

    visited = {}
    q = [start]

    while len(q) != 0:
        nx = q.pop(0)

        h = hash(nx)
        if h in visited: continue
        visited[h] = True

        moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for move in moves:
            nr = nx[R] + move[R]
            nc = nx[C] + move[C]

            h = hash((nr, nc))
            if h in visited: continue

            other = "G" if nx[T] == "E" else "E"

            if grid[nr][nc] == other:
                return nx[S]

            elif grid[nr][nc] == ".":
                q.append( (nr, nc, 1 + nx[S], nx[T]) )

    return float("inf")

def show(grid):
    for row in grid:
        print("".join(row))

def sol(i):
    grid = [list(x.strip()) for x in open("d15.txt").readlines()]

    units = []
    num_e = 0
    num_g = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            x = grid[r][c]
            if x == "E":
                units.append( [r, c, 200, "E", False] )
                num_e += 1
            elif x == "G":
                units.append( [r, c, 200, "G", False] )
                num_g += 1

    turns = 0
    while True:

        # get reading order of remaining units
        units = sorted(units)

        if Z:
            print("num:", num_e, num_g)
            print("turn:", turns)
            show(grid)
            print(units)
            print(list(map(lambda x: x[H], units)))
            print("")

        for unit in units:

            if Z: print("unit:", unit)

            # unit will not take turn if dead
            if unit[D]: continue

            # are all targets dead?
            if num_e == 0 or num_g == 0:
                return turns, sum(map(lambda x: x[H] if not x[D] else 0, units)), num_e, num_g

            # can this unit attack?
            other = "G" if unit[T] == "E" else "E"
            moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            possible = []
            for move in moves:

                nr = unit[R] + move[R]
                nc = unit[C] + move[C]

                #if Z: print(" checking:", nr, nc)

                if grid[nr][nc] == other:
                    possible.append((nr, nc))

            done = False
            if len(possible) > 0:

                result = do_damage(possible, nr, nc, units, grid, i)
                done = True

                # update counts if a unit dies in the attack
                if result:
                    if unit[T] == "E":
                        num_g -= 1
                    else:
                        num_e -= 1

            if done: continue

            # this unit will attempt to move
            m = best_move(unit, grid)
            # if Z: print(" best_move:", m)
            if m != False:
                move_unit(unit, m, grid)

            # can this unit attack now?
            other = "G" if unit[T] == "E" else "E"
            moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            possible = []
            for move in moves:

                nr = unit[R] + move[R]
                nc = unit[C] + move[C]

                #if Z: print(" checking:", nr, nc)

                if grid[nr][nc] == other:
                    possible.append((nr, nc))

            done = False
            if len(possible) > 0:

                result = do_damage(possible, nr, nc, units, grid, i)
                done = True

                # update counts if a unit dies in the attack
                if result:
                    if unit[T] == "E":
                        num_g -= 1
                    else:
                        num_e -= 1

        # remove dead units
        units = list(filter(lambda x: x[H] > 0, units))
        turns += 1

# main
for i in range(3, 100):
    turns, total, elves, gob = sol(i)
    print(turns * total, elves, gob)
    # sys.stdout.flush()


# 138740 too low
