import itertools
mcode = [int(x) for x in open("input.txt").read().split(",")]
#mcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
pc_lst = [0,0,0,0,0]
D = False

def pad(n):
    return "0" * (5 - len(str(n))) + str(n)

def get(code, mode, value):
    return value if mode == 1 else code[value]

def compute(code_lst, code_number, _in, in_index, _out):
    global pc_lst
    code = code_lst[code_number]

    if D: print("in_index, _out:", in_index, _out)

    once = True

    #code = code[:]

    while True:
        _op = [int(c) for c in pad(code[pc_lst[code_number]])]
        op = int(str(_op[-2]) + str(_op[-1]))
        pm3, pm2, pm1 = int(_op[0]), int(_op[1]), int(_op[2])

        p1 = None if len(code) <= (pc_lst[code_number] + 1) else code[pc_lst[code_number] + 1]
        p2 = None if len(code) <= (pc_lst[code_number] + 2) else code[pc_lst[code_number] + 2]
        p3 = None if len(code) <= (pc_lst[code_number] + 3) else code[pc_lst[code_number] + 3]

        if op == 1: # add
            code[p3] = get(code, pm1, p1) + get(code, pm2, p2)
            pc_lst[code_number] += 4

        elif op == 2: # mult
            code[p3] = get(code, pm1, p1) * get(code, pm2, p2)
            pc_lst[code_number] += 4

        elif op == 3: # input
            if in_index < len(_in):
                #code[p1] = int(input("INPUT:"))
                if once:
                    if D: print("INPUT", _in[in_index])
                    code[p1] = _in[in_index]
                    once = False
                else:
                    if D: print("INPUT", _out[-1])
                    code[p1] = _out[-1]
            else:
                if D: print("INPUT", _out[-1])
                code[p1] = _out[-1]
            pc_lst[code_number] += 2

        elif op == 4: # output
            #print("OUTPUT:", get(pm1, p1))
            if D: print("OUTPUT:", get(code, pm1, p1))
            _out.append(get(code, pm1, p1))
            pc_lst[code_number] += 2
            break

        elif op == 99: # halt
            # halt
            return False

        elif op == 5: # jump-if-true
            if get(code, pm1, p1) != 0:
                pc_lst[code_number] = get(code, pm2, p2)
            else:
                pc_lst[code_number] += 3

        elif op == 6: # jump-if-false
            if get(code, pm1, p1) == 0:
                pc_lst[code_number] = get(code, pm2, p2)
            else:
                pc_lst[code_number] += 3

        elif op == 7: # less than
            if get(code, pm1, p1) < get(code, pm2, p2):
                code[p3] = 1
            else:
                code[p3] = 0
            pc_lst[code_number] += 4

        elif op == 8: # halt
            if get(code, pm1, p1) == get(code, pm2, p2):
                code[p3] = 1
            else:
                code[p3] = 0
            pc_lst[code_number] += 4

    return True

def sol():
    global gc_lst
    _out = []
    best = float("-inf")
    for _in in list(itertools.permutations([5,6,7,8,9])):
        _out.clear()
        _out.append(0)
        in_index = 0
        code_number = 0
        code_lst = [mcode[:], mcode[:], mcode[:], mcode[:], mcode[:]]
        pc_lst.clear()
        for _ in range(5): pc_lst.append(0)
        while True:
            if compute(code_lst, code_number, _in, in_index, _out) == False:
                break
            #print(_out[-1])
            in_index += 1
            code_number = (code_number + 1) % 5

        best = max(best, _out[-1])
        #print("best:", best)
    return best

ans = sol()
print(ans)
