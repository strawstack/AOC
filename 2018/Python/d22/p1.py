import sys

ROCKY  = 0
WET    = 1
NARROW = 2

def hash(r, c):
    return (r, c)

def getGeologicIndex(r, c, erosion_levels, tr, tc):

    # start
    if r == 0 and c == 0: return 0

    # target
    if r == tr and c == tc: return 0

    if r == 0: return c * 16807
    if c == 0: return r * 48271

    return erosion_levels[hash(r, c - 1)] * erosion_levels[hash(r - 1, c)]

def getErosionLevel(geo_index, depth, number):
    return (geo_index + depth) % 20183

def getType(erosion_level):

    value = erosion_level % 3

    if value == 0:
        return ROCKY

    elif value == 1:
        return WET

    else: # value == 2
        return NARROW

def sol():
    data = [x.strip() for x in open("d22.txt").readlines()]
    depth = int(data[0].split(" ")[1])
    tc, tr = [int(x) for x in data[1].split(" ")[1].split(",")]

    cave = {}
    erosion_levels = {}
    total = 0
    for r in range(0, tr + 1):
        for c in range(0, tc + 1):

            geo_index = getGeologicIndex(r, c, erosion_levels, tr, tc)
            erosion_level = getErosionLevel(geo_index, depth, 20183)
            erosion_levels[hash(r, c)] = erosion_level
            r_type = getType(erosion_level)

            total += r_type

    return total

# main
ans = sol()
print(ans)
# sys.stdout.flush()
