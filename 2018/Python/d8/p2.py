import sys
#sys.setrecursionlimit(1000)

# returns total, remaining list
def getNode(list):

    c = list[0]
    m = list[1]

    if c == 0:
        return sum(list[2:2+m]), list[2+m:]

    children = []
    list = list[2:]
    for i in range(c):
        pt, list = getNode(list)
        children.append(pt)

    final_total = 0
    for v in list[:m]:
        if v == 0: continue
        if v <= c:
            final_total += children[v-1]

    return final_total, list[m:]


def sol():
    # 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    data = [int(x) for x in open("d8.txt").read().strip().split(" ")]

    total, _ = getNode(data)

    return total


# main
ans = sol()
print(ans)


# 39446
