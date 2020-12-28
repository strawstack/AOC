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

    lst1 = []
    lst2 = []

    name = "YOU"
    while name in tree:
        name = tree[name]
        lst1.append(name)

    name = "SAN"
    while name in tree:
        name = tree[name]
        lst2.append(name)

    for i in range(len(lst1)):
        link = lst1[i]
        if link in lst2:
            return i + lst2.index(link)


ans = sol()
print(ans)
