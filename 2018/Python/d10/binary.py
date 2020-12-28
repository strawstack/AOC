import math

X  = 0
Y  = 1
VX = 2
VY = 3

# estimate centre location
def centre(particles):
    n = len(particles)
    ax = 0
    ay = 0
    for p in particles:
        ax += p[X]
        ay += p[Y]
    return (ax/n, ay/n)

# total distance from every particle to centre point
def distance(particles, m):
    total = 0
    c = centre(particles)
    for p in particles:
        cx = p[X] + p[VX] * m
        cy = p[Y] + p[VY] * m
        total += math.sqrt( math.pow(cx  - c[X], 2) + math.pow(cy - c[Y], 2) )
    return total

def sol():
    # position=<-50429,  40580> velocity=< 5, -4>
    data = [x.strip() for x in open("d10.txt").readlines()]

    particles = []
    for row in data:
        one, two, _ = row.split(">")
        a, b = one.split(",")
        _, a = a.split("<")
        x = int(a)
        y = int(b)
        _, two = two.split("<")
        a, b = two.split(",")
        vx = int(a)
        vy = int(b)
        particles.append( [x, y, vx, vy] )

    low = 0
    hi  = 15000

    while low <= hi:
        m = (low + hi)//2

        d1 = distance(particles, m)
        d2 = distance(particles, m + 1)

        if d1 < d2:
            hi = m - 1

        else:
            low = m + 1

    return m

# main
ans = sol()
print(ans)
