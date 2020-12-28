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

    funct = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    ops = []
    total = 0
    for row in data:
        before = [int(x) for x in input().split(": ")[1][1:-1].split(", ")]
        instc  = [int(x) for x in input().split(" ")]
        after  = [int(x) for x in input().split(":  ")[1][1:-1].split(", ")]

        count = 0
        for f in funct:
            reg = before[:]
            f(instc[1], instc[2], instc[3], reg)
            if reg == after:
                count += 1

        if count >= 3:
            total += 1

        x = input() # newline
        if x == "END": break

    return total

# main
ans = sol()
print(ans)
# sys.stdout.flush()

# 671 no
# 672 no
