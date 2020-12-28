orbits = [x[:-1].split(")") for x in open("input.txt").readlines()]

def sol():

    tree = {}
    lst = []

    for orbit in orbits:
        tree[orbit[1]] = orbit[0]

        lst.append(orbit[0])
        lst.append(orbit[1])

    # Rem duplicates
    lst = list(set(lst))

    count = 0
    for name in lst:

        while name in tree:
            name = tree[name]
            count += 1

    return count


ans = sol()
print(ans)
