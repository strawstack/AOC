code = [int(x) for x in open("input.txt").read().split(",")]

def sol():
    pc = 0

    code[1] = 12
    code[2] = 2

    while code[pc] != 99:
        op = code[pc]
        a  = code[pc + 1]
        b  = code[pc + 2]
        out = code[pc + 3]

        if op == 1:
            code[out] = code[a] + code[b]

        elif op == 2:
            code[out] = code[a] * code[b]

        else:
            print("something went wrong!")
            print("op:", op)
            return None

        pc += 4

    return code[0]


ans = sol()
print(ans)
