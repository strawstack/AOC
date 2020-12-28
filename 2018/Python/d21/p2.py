import sys

seen = {}

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
    data = [x.strip() for x in open("d19.txt").readlines()]
    pcr = int(data[0].split(" ")[1])

def sol():
    data = [x.strip() for x in open("d21.txt").readlines()]
    pcr = int(data[0].split(" ")[1])

    instc = {
        "addr": addr,
        "addi": addi,
        "mulr": mulr,
        "muli": muli,
        "banr": banr,
        "bani": bani,
        "borr": borr,
        "bori": bori,
        "setr": setr,
        "seti": seti,
        "gtir": gtir,
        "gtri": gtri,
        "gtrr": gtrr,
        "eqir": eqir,
        "eqri": eqri,
        "eqrr": eqrr
    }

    lines = []
    for line in data[1:]:
        c = line.split(" ")
        lines.append([instc[c[0]], int(c[1]), int(c[2]), int(c[3]), c[0]])

    reg = [13, 0, 0, 0, 0, 0]
    reg = [13, 65536, 0, 24, 10626258, 255]

    # 10961197

    while reg[pcr] >= 0 and reg[pcr] < len(lines):

        # get pc
        pc = reg[pcr]

        # execute line
        lines[pc][0]( lines[pc][1], lines[pc][2], lines[pc][3], reg )

        #print("L" + str(pc) + ":" , lines[pc][4], lines[pc][1], lines[pc][2], lines[pc][3])

        # increment pc
        reg[pcr] += 1

        #print("pc:", reg[pcr])
        #print(reg, end="\n")
        #_ = input()

        # injection
        if reg[pcr] == 18:
            reg[5] = reg[1] // 256

        if reg[pcr] == 28:
            if reg[4] in seen:
                return reg[4]
            seen[reg[4]] = True
            print("r4:", reg[4])

    return reg

# main
ans = sol()
print(ans)
# sys.stdout.flush()
