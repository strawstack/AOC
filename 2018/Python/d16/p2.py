import sys

def addr(rA, rB, rC, reg):
    reg[rC] = reg[rA] + reg[rB]

def addi(rA, iB, rC, reg):
    reg[rC] = reg[rA] + iB

def mulr(rA, rB, rC, reg):
    reg[rC] = reg[rA] * reg[rB]

def muli(rA, iB, rC, reg):
    reg[rC] = reg[rA] * iB

def banr(rA, rB, rC, reg):
    reg[rC] = reg[rA] & reg[rB]

def bani(rA, iB, rC, reg):
    reg[rC] = reg[rA] & iB

def borr(rA, rB, rC, reg):
    reg[rC] = reg[rA] | reg[rB]

def bori(rA, iB, rC, reg):
    reg[rC] = reg[rA] | iB

def setr(rA, _, rC, reg):
    reg[rC] = reg[rA]

def seti(iA, _, rC, reg):
    reg[rC] = iA

def gtir(iA, rB, rC, reg):
    reg[rC] = 1 if iA > reg[rB] else 0

def gtri(rA, iB, rC, reg):
    reg[rC] = 1 if reg[rA] > iB else 0

def gtrr(rA, rB, rC, reg):
    reg[rC] = 1 if reg[rA] > reg[rB] else 0

def eqir(iA, rB, rC, reg):
    reg[rC] = 1 if iA == reg[rB] else 0

def eqri(rA, iB, rC, reg):
    reg[rC] = 1 if reg[rA] == iB else 0

def eqrr(rA, rB, rC, reg):
    reg[rC] = 1 if reg[rA] == reg[rB] else 0

def sol():
    data = [x.strip() for x in open("d16.txt").readlines()]

    # b[x] x is opcode value is list of [fz, index]
    b = [[] for x in range(16)]
    for i in range(16):
        for j in range(16):
            b[i].append([0, j])


    funct = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    map = [2, 0, 4, 13, 3, 8, 14, 11, 15, 1, 10, 12, 6, 5, 9, 7]

    ops = []
    for row in data:
        before = [int(x) for x in input().split(": ")[1][1:-1].split(", ")]
        instc  = [int(x) for x in input().split(" ")]
        after  = [int(x) for x in input().split(":  ")[1][1:-1].split(", ")]

        for i, f in enumerate(funct):
            reg = before[:]
            f(instc[1], instc[2], instc[3], reg)
            if reg == after:
                b[instc[0]][i][0] += 1 # this opcode behaves like i

        x = input() # newline
        if x == "END": break

    test = [[int(y) for y in x.strip().split(" ")] for x in open("prog.txt").readlines()]

    op = [None for x in range(16)]
    for i in range(16):        
        op[i] = funct[map[i]]

    reg = [0, 0, 0, 0]
    for line in test:
        op[line[0]](line[1], line[2], line[3], reg)

    return reg

# main
ans = sol()
print(ans)
# sys.stdout.flush()

# 1 no
