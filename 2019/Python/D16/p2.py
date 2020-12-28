import sys
lst = [int(x) for x in list(open("input.txt").read()[:-1])]
lst = lst * 10000
D = False

def fft(lst):
    outlst = []
    total = sum(lst)
    for i in range(len(lst)):
        outlst.append(abs(total) % 10)
        total -= lst[i]
    return outlst

def sol(lst):
    baseline = int("".join([str(x) for x in lst[:7]]))
    print("baseline:", baseline)
    lst = lst[baseline:]
    for i in range(100):
        if D: print("lst:", lst)
        lst = fft(lst)
        print(i)
        sys.stdout.flush()
    if D: print("lst:", lst)
    return lst[:8]

ans = sol(lst)
print(ans)
