import sys

def sol():
    # data = [x.strip() for x in open("d14.txt").readlines()]

    #skill = 260321 + 10
    data  = 260321
    skill = data + 10

    res = [3, 7]
    elf1 = 0
    elf2 = 1

    while skill > 0:
        v1 = res[elf1]
        v2 = res[elf2]

        # new res list
        new = [int(x) for x in str(v1 + v2)]

        # add new res
        res += new

        if len(res) >= data + 10:
            return res[data:data + 10]

        # move
        elf1 = (1 + v1 + elf1) % len(res)
        elf2 = (1 + v2 + elf2) % len(res)
        skill -= 1

    #print(res)

# main
ans = sol()
print("".join([str(x) for x in ans]))
# sys.stdout.flush()
