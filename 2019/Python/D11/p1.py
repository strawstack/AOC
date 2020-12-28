# import itertools

D = False

_code = [int(x) for x in open("input.txt").read().strip().split(",")]
code = {}

grid = {}
grid[(0,0)] = 0

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

def compute():

    global code
    global pc
    global base
    global grid

    pc = 0
    base = 0
    location = [0, 0]
    direction = 0 # 0 up, 1 right, 2 down, 3 left
    first = True

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
            if (location[0], location[1]) in grid:
                code[get(pm1, p1, True)] = grid[(location[0], location[1])]
            else:
                code[get(pm1, p1, True)] = 0
            pc += 2

        elif op == 4: # output
            #if D: print("OUTPUT:", get(pm1, p1))
            if first:
                first = False
                grid[(location[0], location[1])] = get(pm1, p1)
            else:
                first = True
                if get(pm1, p1) == 0:
                    direction = (direction - 1) % 4
                else:
                    direction = (direction + 1) % 4

                # Move one space
                offset = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                location[0] += offset[direction][0]
                location[1] += offset[direction][1]
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

def sol():
    global grid
    compute()
    return len(grid)

ans = sol()
print(ans)
