code = [int(x) for x in open("input.txt").read().split(",")]
copy = code[:]

FIND = 19690720

def sol():

    for one in range(99):
        for two in range(99):

            pc = 0
            code = copy[:]
            while code[pc] != 99:

                code[1] = one
                code[2] = two

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
                    return (None, None)

                pc += 4

            if code[0] == FIND:
                return (one, two)

a, b = sol()
print(100 * a + b)
