X  = 0
Y  = 1
VX = 2
VY = 3

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

    estimates = []
    for i in range(len(particles) - 1):
        one = particles[i]
        two = particles[i + 1]

        one_m = one[VY]/one[VX]
        two_m = two[VY]/two[VX]

        one_b = one[Y] - one_m * one[X]
        two_b = two[Y] - two_m * two[X]

        # find intersection
        try:
            inter_x = (two_b - one_b) / (one_m - two_m)
        except:
            pass # div by zero

        # time to intersection
        estimate = abs(inter_x - one[X]) / abs(one[VX])
        estimates.append(estimate)

        print(str(len(estimates)) + ",", sum(estimates) / len(estimates))

# main
ans = sol()
print(ans)
