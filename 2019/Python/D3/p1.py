lines = [x[:-1] for x in open("input.txt").readlines()]
w1, w2 = lines[0], lines[1]

w1 = w1.split(",")
w2 = w2.split(",")

def hash(coord):
    return str(coord[0]) + ":" + str(coord[1])

def mapWire(wire):
    coord = [0, 0]
    map = {}

    for part in wire:
        dir = part[0]
        dist = int(part[1:])

        if dir == "U":
            for _ in range(dist):
                map[hash(coord)] = True
                coord[1] += 1

        elif dir == "R":
            for _ in range(dist):
                map[hash(coord)] = True
                coord[0] += 1

        elif dir == "D":
            for _ in range(dist):
                map[hash(coord)] = True
                coord[1] -= 1

        else: # dir == "L"
            for _ in range(dist):
                map[hash(coord)] = True
                coord[0] -= 1

    return map

def sol():
    m1 = mapWire(w1)

    hit = []
    coord = [0, 0]

    for part in w2:
        dir = part[0]
        dist = int(part[1:])

        if dir == "U":
            for _ in range(dist):
                if hash(coord) in m1:
                    hit.append([coord[0], coord[1]])
                coord[1] += 1

        elif dir == "R":
            for _ in range(dist):
                if hash(coord) in m1:
                    hit.append([coord[0], coord[1]])
                coord[0] += 1

        elif dir == "D":
            for _ in range(dist):
                if hash(coord) in m1:
                    hit.append([coord[0], coord[1]])
                coord[1] -= 1

        else: # dir == "L"
            for _ in range(dist):
                if hash(coord) in m1:
                    hit.append([coord[0], coord[1]])
                coord[0] -= 1

    # find the closest distance
    best = float("inf")
    best_index = 0
    for i in range(len(hit)):
        h = hit[i]
        dist = abs(h[0]) + abs(h[1])

        if h[0] == 0 and h[1] == 0:
            continue

        if dist < best:
            best_index = i
            best = dist

    return best

ans = sol()
print(ans)
