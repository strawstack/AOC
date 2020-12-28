code = [int(x) for x in open("input.txt").read().split(",")]
D = False

def pad(n):
    return "0" * (5 - len(str(n))) + str(n)

def get(mode, value):
    return value if mode == 1 else code[value]

def sol():
    pc = 0
    while True:
        if D: input("*** Enter to Step ***")
        if D: print("pc:", pc)

        _op = [int(c) for c in pad(code[pc])]
        op = int(_op[-2] + _op[-1])
        pm3, pm2, pm1 = int(_op[0]), int(_op[1]), int(_op[2])

        p1 = None if len(code) <= (pc + 1) else code[pc + 1]
        p2 = None if len(code) <= (pc + 2) else code[pc + 2]
        p3 = None if len(code) <= (pc + 3) else code[pc + 3]

        if D:
            print("_op:", _op, " op:" , op)
            print("pm1:", pm1, " pm2:", pm2, " pm3:", pm3)
            print("p1:", p1, " p2:", p2, " p3:", p3)

        if op == 1: # add
            code[p3] = get(pm1, p1) + get(pm2, p2)
            pc += 4

        elif op == 2: # mult
            code[p3] = get(pm1, p1) * get(pm2, p2)
            pc += 4

        elif op == 3: # input
            code[p1] = int(input("INPUT:"))
            pc += 2

        elif op == 4: # output
            print("OUTPUT:", get(pm1, p1))
            pc += 2

        elif op == 99: # halt
            # halt
            break
            
    print("halt")

ans = sol()
print(ans)
