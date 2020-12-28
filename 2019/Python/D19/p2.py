# import itertools

D = False

_code = [int(x) for x in open("input.txt").read().strip().split(",")]
my_code = {}

for i in range(len(_code)):
    my_code[i] = _code[i]

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

def compute(lst):

    global code
    global pc
    global base

    code = {}
    for key in my_code:
        code[key] = my_code[key]

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
            code[get(pm1, p1, True)] = lst.pop(0)
            pc += 2

        elif op == 4: # output
            if D: print("OUTPUT:", get(pm1, p1))
            return get(pm1, p1)
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

def check(loc):
    # Return if the cube fits with left edge
    # in this column
    cur = loc[:]
    while True:
        v1 = compute(cur[:])
        v2 = compute([cur[0], cur[1] + 1])
        if v2 == 0:
            break
        else:
            cur = [cur[0], cur[1] + 1]
    top_left = compute([cur[0], cur[1] - 99])
    top_right = compute([cur[0] + 99, cur[1] - 99])
    if top_left == 1 and top_right == 1:
        return [cur[0], cur[1] - 99]
    else:
        return False

def sol():

    RIGHT = True # Toggles right and down
    loc = [291, 522] # [12, 19] # Location of drone
    down_count = 0 # Track depth of ray at column

    # Move RIGHT/DOWN until we find
    # a column greater than 100 in depth
    while True:
        if RIGHT:
            print("RIGHT:", loc)
            ans = check(loc[:])
            if ans != False:
                return ans
            v1 = compute(loc[:])
            v2 = compute([loc[0] + 1, loc[1]])
            if v2 == 0:
                RIGHT = False
            else:
                loc = [loc[0] + 1, loc[1]]
        else: # DOWN
            print("DOWN:", loc)
            v1 = compute(loc[:])
            v2 = compute([loc[0], loc[1] + 1])
            if v2 == 0:
                RIGHT = True
                print("down_count:", down_count, flush=True)
                down_count = 0
            else:
                loc = [loc[0], loc[1] + 1]
                down_count += 1

    return None

# [291, 522] first column with >= 100 depth
# ans: 6671097
ans = sol()
print(str(ans[0] * 10000) + ans[1])
