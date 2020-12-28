import math

field = [x[:-1] for x in open("input2.txt").readlines()]

def collinear(p1, p2, p3):
    # If area of triangle is zero
    # https://www.urbanpro.com/gre/how-to-determine-if-points-are-collinear
    return (0.5 * ( ((p1[1] - p2[1]) * (p2[2] - p3[2])) - ((p1[2] - p2[2]) * (p2[1] - p3[1])) )) == 0

def number(a, astr):
    # How many can "a" see
    vect = []
    for b in astr:
        if a[0] == b[0] and a[1] == b[1]:
            continue
        mag = math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))
        vect.append( (mag, b[0], b[1]) )

    vect = sorted(vect)
    total = 0

    # Can "a" see v1
    for v1 in vect:

        # If the next closest collinear point
        # is further away then we can see it
        # Or if there are no collinear points
        coPoint = False
        for v2 in vect:
            if v1[1] == v2[1] and v1[2] == v2[2]:
                continue

            # Check if "a" can see v1
            # By finding all colinear points and ensuring v1 is the closest
            if collinear((0, a[0], a[1]), v1, v2):
                coPoint = True
                if v1[0] < v2[0]:
                    total += 1
                break

        if not coPoint:
            total += 1

    return total

def sol():
    # Convert field to astr
    astr = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "#":
                astr.append( (x, y) )

    # For each asteroid
    # Find "reduced" tuples for all others
    # If reduced tuples are the same, discard
    # Count length of result
    best = float("-inf")
    for a in astr:
        best = max(best, number(a, astr))

    return best

ans = sol()
print(ans)
