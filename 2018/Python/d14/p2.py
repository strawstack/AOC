import sys

def sol():
    # data = [x.strip() for x in open("d14.txt").readlines()]

    #skill = 260321 + 10
    data  = 260321
    skill = data + 10

    pat = "260321"
    p = 0

    res = [3, 7]
    elf1 = 0
    elf2 = 1

    while True:
        v1 = res[elf1]
        v2 = res[elf2]

        # new res list
        new = [int(x) for x in str(v1 + v2)]

        # add new res
        res += new

        # search for the sequence
        n = list(str(v1 + v2))
        done = False
        for digit in n:
            if pat[p] == digit:
                p += 1
                if p == len(pat):
                    done = True
                    break
            else:
                p = 0

        if done:
            return len(res), res[-10:]

        # move
        elf1 = (1 + v1 + elf1) % len(res)
        elf2 = (1 + v2 + elf2) % len(res)
        skill -= 1

    #print(res)

# main
ans, ans2 = sol()
print(ans)
print(ans2)
# sys.stdout.flush()
