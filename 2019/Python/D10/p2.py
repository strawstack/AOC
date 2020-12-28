import math

field = [x[:-1] for x in open("input.txt").readlines()]
D = False

if D:
    s = 0
    for row in field:
        s += row.count("#")
    print("astr count:", s)

def mag(a, b):
    return math.sqrt(math.pow(a[1] - b[1], 2) + math.pow(a[0] - b[0], 2))

def computeGCD(x, y):
    gcd = 1
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

def lowestMatch(p1, p2, debug=False):
    if debug: print("lowestMatch", p1, p2)
    g1 = computeGCD(abs(p1[0]), abs(p1[1]))
    g2 = computeGCD(abs(p2[0]), abs(p2[1]))
    p1 = (p1[0] // g1, p1[1] // g1)
    p2 = (p2[0] // g2, p2[1] // g2)
    if debug: print("found", p1, p2)
    return p1 == p2

def show(a, b, c):
    for y in range(len(field)):
        for x in range(len(field[y])):
            if (x, y) == a:
                print("A", end=" ")

            elif (x, y) == b:
                print("B", end=" ")

            elif (x, y) == c:
                print("C", end=" ")

            else:
                print(".", end=" ")
        print("")

def vapor(a, astr, skip):
    count = 0
    notblock = {}
    lst = []
    for b in astr:
        if b == a: continue
        if b in skip: continue
        blocked = False
        for c in astr:
            if c == a or c == b: continue
            if c in skip: continue

            # Does c block b?
            if (b[0] - a[0]) == 0:
                if c[0] == a[0]:
                    if (c[1] < b[1] and c[1] > a[1]) or (c[1] < a[1] and c[1] > b[1]):
                        if D:
                            print("a:", a)
                            print("b:", b)
                            print("c:", c)
                            show(a, b, c)
                            print("1")
                        blocked = True
                        break

            elif (b[1] - a[1]) == 0:
                if c[1] == a[1]:
                    if (c[0] < b[0] and c[0] > a[0]) or (c[0] < a[0] and c[0] > b[0]):
                        if D:
                            print("a:", a)
                            print("b:", b)
                            print("c:", c)
                            show(a, b, c)
                            print("2")
                        blocked = True
                        break

            else:
                if lowestMatch((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1])):
                    if mag(a, c) < mag(a, b):
                        one = (-1 if c[0] < 0 else 1, -1 if c[1] < 0 else 1)
                        two = (-1 if b[0] < 0 else 1, -1 if b[1] < 0 else 1)
                        if one == two:
                            if D:
                                lowestMatch((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]), True)
                                print("a:", a)
                                print("b:", b)
                                print("c:", c)
                                show(a, b, c)
                                print("3")
                            blocked = True
                            break

        if not blocked:
            notblock[b] = True
            lst.append((b[0] - a[0], a[1] - b[1], b[0], b[1]))
            count += 1

    if False:
        for y in range(len(field)):
            for x in range(len(field[y])):
                if (x, y) in notblock:
                    print("#", end=" ")
                else:
                    if a == (x, y):
                        print("@", end=" ")
                    else:
                        print(".", end=" ")
            print("")

    return lst

def deg(rad):
    return 180 * (rad / math.pi)

def angle(coord):
    x = -1 * coord[0]
    y = coord[1]
    ans = deg(math.atan2(y, x))
    ans -= 90
    if ans < 0:
        return 360 + ans
    return ans

def sol():
    # Convert field to astr
    astr = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "#":
                astr.append( (x, y) )

    coord = (19, 11)
    #coord = (11, 13)
    count = 1
    skip = {}

    flag = True
    while flag:
        # List of next to vapor
        lst = vapor(coord, astr, skip)
        for item in lst:
            skip[item] = True

        # Find the number of each in lst using angles
        lst = sorted(map(lambda x: (angle(x), x), lst))
        for item in lst:
            print(count, item)
            count += 1
            if count > 200:
                flag = False
                break

    return None

ans = sol()
print(ans)
