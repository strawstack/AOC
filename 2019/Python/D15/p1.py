import random
import json
import time
D = False

_code = [int(x) for x in open("input.txt").read().strip().split(",")]
code = {}

for i in range(len(_code)):
    code[i] = _code[i]

pc = 0
base = 0

def pad(n):
    return "0" * (5 - len(str(n))) + str(n)

def get(mode, value, left=False):
    global base
    if mode == 0:
        if value not in code: code[value] = 0
        return code[value] if left == False else value

    elif mode == 1:
        return value

    elif mode == 2:
        if (value + base) not in code: code[value + base] = 0
        return code[value + base] if left == False else value + base

def hash(t):
    return str(t[0]) + ":" + str(t[1])

def hash_to_coord(h):
    x, y = h.split(":")
    return int(x), int(y)

def render(grid, droid):
    print("\033[2J")
    min_x, max_x = -20, 20
    min_y, max_y = -20, 20
    for key in grid:
        cx, cy = hash_to_coord(key)
        min_x = min(min_x, cx)
        max_x = max(max_x, cx)
        min_y = min(min_y, cy)
        max_y = max(max_y, cy)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            h = hash((x,y))

            if x == droid[0] and y == droid[1]:
                print("D", end=" ")

            elif h in grid:
                if grid[h] == 1:
                    print(" ", end=" ")
                elif grid[h] == 0:
                    print("#", end=" ")
                else:
                    print("K", end=" ")
            else:
                print(".", end=" ")
        print("")
    print("")

def bfs(grid):
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    seen = {}

    q = [(0, 0, 0)]
    while len(q) > 0:
        cx, cy, d = q.pop(0)
        if (cx, cy) in seen: continue
        seen[(cx, cy)] = True

        for ox, oy in adj:
            nx, ny = cx + ox, cy + oy

            if hash((nx, ny)) in grid:
                if grid[hash((nx, ny))] == 1:
                    q.append((nx, ny, d + 1))

                elif grid[hash((nx, ny))] == 2:
                    return d
    return -1

def compute():

    grid = {}
    droid = [0, 0]
    lastInput = 0
    framecount = 0
    count = 1000
    move = {
        1: (0, -1), # North
        2: (0, 1),  # South
        3: (-1, 0), # West
        4: (1, 0)   # East
    }

    global code
    global pc
    global base

    pc = 0
    base = 0

    while True:

        if D: print("code:", code)
        if D: print("pc:", pc)

        if pc not in code: code[pc] = 0
        _op = [int(c) for c in pad(code[pc])]

        op = int(str(_op[-2]) + str(_op[-1]))
        pm3, pm2, pm1 = int(_op[0]), int(_op[1]), int(_op[2])

        if (pc + 1) not in code: code[pc + 1] = 0
        if (pc + 2) not in code: code[pc + 2] = 0
        if (pc + 3) not in code: code[pc + 3] = 0
        p1 = code[pc + 1]
        p2 = code[pc + 2]
        p3 = code[pc + 3]

        if D: print("op:", op)
        if D: print("pm3, pm2, pm1:", pm3, pm2, pm1)
        if D: print("p3, p2, p1:", p3, p2, p1)
        if D: print("base:", base, "pc:", pc)

        if op == 1: # add
            code[get(pm3, p3, True)] = get(pm1, p1) + get(pm2, p2)
            pc += 4

        elif op == 2: # mult
            code[get(pm3, p3, True)] = get(pm1, p1) * get(pm2, p2)
            pc += 4

        elif op == 3: # input
            dir = {
                "w": 1,
                "a": 3,
                "s": 2,
                "d": 4
            }
            _in = False
            if count > 0:
                count -= 1
                _in = random.randrange(1, 4 + 1)
            else:
                while _in not in dir:
                    _in = input("Input:")
                    if _in == "z":
                        count = 1000
                        _in = 1
                        break
            if _in in dir:
                _in = dir[_in]
            code[get(pm1, p1, True)] = _in
            lastInput = _in
            pc += 2

        elif op == 4: # output
            out = get(pm1, p1)

            if out == 0:
                if hash((droid[0], droid[1])) not in grid:
                    grid[hash((droid[0], droid[1]))] = 1
                ox, oy = move[lastInput]
                nx, ny = droid[0] + ox, droid[1] + oy
                grid[hash((nx, ny))] = 0

            elif out == 1:
                if hash((droid[0], droid[1])) not in grid:
                    grid[hash((droid[0], droid[1]))] = 1
                ox, oy = move[lastInput]
                droid[0] += ox
                droid[1] += oy

            elif out == 2:
                if hash((droid[0], droid[1])) not in grid:
                    grid[hash((droid[0], droid[1]))] = 1
                ox, oy = move[lastInput]
                droid[0] += ox
                droid[1] += oy
                if hash((droid[0], droid[1])) not in grid:
                    grid[hash((droid[0], droid[1]))] = 2

            f = open("grid.json", 'w')
            f.write(json.dumps(grid))
            f.close()
            render(grid, droid)
            pc += 2

        elif op == 99: # halt
            # halt
            break

        elif op == 5: # jump-if-true
            if get(pm1, p1) != 0:
                pc = get(pm2, p2)
            else:
                pc += 3

        elif op == 6: # jump-if-false
            if get(pm1, p1) == 0:
                pc = get(pm2, p2)
                if D: print("6 pc:", pc)
            else:
                pc += 3

        elif op == 7: # less than
            if get(pm1, p1) < get(pm2, p2):
                code[get(pm3, p3, True)] = 1
            else:
                code[get(pm3, p3, True)] = 0
            pc += 4

        elif op == 8: # halt
            if get(pm1, p1) == get(pm2, p2):
                code[get(pm3, p3, True)] = 1
            else:
                code[get(pm3, p3, True)] = 0
            pc += 4

        elif op == 9:
            base += get(pm1, p1)
            pc += 2

    length = bfs(grid)
    return length

def sol():
    return compute()

ans = sol()
print(ans)
