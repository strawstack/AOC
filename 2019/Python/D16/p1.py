import sys
lst = [int(x) for x in list(open("input.txt").read()[:-1])]
D = False

def fft(lst):
    base = [0, 1, 0, -1]
    outlst = []

    i = 0
    while i < len(lst):
        # i is the index into output

        # skip first once
        # each digit of pattern will repeat count times
        first = True
        count = i + 1
        c_count = count
        current_base = 0

        # For each digit of lst...
        value = 0 # the current out value
        k = 0
        while k < len(lst):
            if first:
                first = False
                c_count -= 1
            if c_count > 0:
                if D: print(lst[k], base[current_base])
                value += lst[k] * base[current_base]
                c_count -= 1
                k += 1
            else:
                current_base = (current_base + 1) % 4
                c_count = count
        outlst.append(abs(value) % 10)
        i += 1

    return outlst

def sol(lst):
    for i in range(100):
        if D: print("lst:", lst)
        lst = fft(lst)
        print(i)
        sys.stdout.flush()
    if D: print("lst:", lst)
    return lst[:8]

ans = sol(lst)
print(ans)
