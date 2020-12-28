# import itertools
D = False

_code = [int(x) for x in open("input.txt").read().strip().split(",")]
code = {}

for i in range(len(_code)):
    code[i] = _code[i]

code[0] = 2

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

def renderGrid(grid, score):
    mx, my = 0, 0
    for key in grid:
        x, y = key
        mx = max(mx, x)
        my = max(my, y)

    print("\n" * (2 * my))

    print("")
    print("Score:", score)
    print("")
    space = ""
    for c in range(my):
        for r in range(mx + 1):
            if grid[(r, c)] == 0:
                print(" ", end=space)

            elif grid[(r, c)] == 1:
                print("#", end=space)

            elif grid[(r, c)] == 2:
                print("\u2588", end=space)

            elif grid[(r, c)] == 3:
                print("\u2588", end=space)

            elif grid[(r, c)] == 4:
                print("\u25EF", end=space)
        print("")
    print("")

def compute():

    global code
    global pc
    global base

    pc = 0
    base = 0

    grid = {}
    score = 0
    x, y, t = 0, 0, 0
    step = 0

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
            input("INPUT:")

            # Stay in line with the ball
            bx, by = 0, 0
            px, py = 0, 0
            for key in grid:
                if grid[key] == 4:
                    bx, by = key
                elif grid[key] == 3:
                    px, py = key

            print(bx, by)
            print(px, py)

            if bx == px:
                code[get(pm1, p1, True)] = 0
            else:
                code[get(pm1, p1, True)] = -1 if bx < px else 1

            pc += 2

        elif op == 4: # output
            #print("OUTPUT:", get(pm1, p1))
            #if D: print("OUTPUT:", get(pm1, p1))
            if step == 0:
                x = get(pm1, p1)

            elif step == 1:
                y = get(pm1, p1)

            elif step == 2:
                t = get(pm1, p1)
                if x == -1 and y == 0:
                    score = t
                else:
                    grid[(x, y)] = t
                renderGrid(grid, score)

            pc += 2
            step = (step + 1) % 3

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
    return grid

def sol():
    grid = compute()
    total = 0
    for key in grid:
        if grid[key] == 2:
            total += 1
    return total

ans = sol()
print(ans)
