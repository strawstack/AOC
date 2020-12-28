import itertools
code = [int(x) for x in open("input.txt").read().split(",")]
#code = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#code = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
#code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
D = False

def pad(n):
    return "0" * (5 - len(str(n))) + str(n)

def get(mode, value):
    return value if mode == 1 else code[value]

def compute(_in, in_index, _out):

    if D: print("in_index, _out:", in_index, _out)

    global code
    code = code[:]
    pc = 0

    once = True

    while True:
        _op = [int(c) for c in pad(code[pc])]
        op = int(_op[-2] + _op[-1])
        pm3, pm2, pm1 = int(_op[0]), int(_op[1]), int(_op[2])

        p1 = None if len(code) <= (pc + 1) else code[pc + 1]
        p2 = None if len(code) <= (pc + 2) else code[pc + 2]
        p3 = None if len(code) <= (pc + 3) else code[pc + 3]

        if op == 1: # add
            code[p3] = get(pm1, p1) + get(pm2, p2)
            pc += 4

        elif op == 2: # mult
            code[p3] = get(pm1, p1) * get(pm2, p2)
            pc += 4

        elif op == 3: # input
            if once:
                #code[p1] = int(input("INPUT:"))
                if D: print("INPUT", _in[in_index])
                code[p1] = _in[in_index]
                once = False
            else:
                if D: print("INPUT", _out[-1])
                code[p1] = _out[-1]
            pc += 2

        elif op == 4: # output
            #print("OUTPUT:", get(pm1, p1))
            if D: print("OUTPUT:", get(pm1, p1))
            _out.append(get(pm1, p1))
            pc += 2
            break

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
            else:
                pc += 3

        elif op == 7: # less than
            if get(pm1, p1) < get(pm2, p2):
                code[p3] = 1
            else:
                code[p3] = 0
            pc += 4

        elif op == 8: # halt
            if get(pm1, p1) == get(pm2, p2):
                code[p3] = 1
            else:
                code[p3] = 0
            pc += 4

def sol():
    _out = []
    best = float("-inf")
    for _in in list(itertools.permutations([0,1,2,3,4])):
        _out.clear()
        _out.append(0)
        in_index = 0
        for _ in range(5):
            compute(_in, in_index, _out)
            in_index += 1
        best = max(best, _out[-1])
    return best

ans = sol()
print(ans)
