import sys
import math

X  = 0
Y  = 1
VX = 2
VY = 3

smallest = float("inf")

def print_letters(particles):

    low_x  = float("inf")
    low_y  = float("inf")

    for p in particles:
        low_x = min(low_x, p[X])
        low_y = min(low_x, p[Y])

    for p in particles:
        p[X] -= low_x
        p[Y] -= low_y

    # print(low_x, low_y) # 140, 109
    grid = [[0 for y in range(65)] for x in range(65)]
    for p in particles:
        grid[p[X]][p[Y]] = 1

    for row in grid:
        for cell in row:
            if cell == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print("")

def update(particles):
    global smallest

    low_x  = float("inf")
    high_x = float("-inf")

    speed = 1

    for p in particles:
        p[X] += p[VX] * speed
        p[Y] += p[VY] * speed

        low_x  = min(low_x, p[X])
        high_x = max(high_x, p[X])

    smallest = min(smallest, abs(low_x - high_x))

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

    x = 100000
    tick = 0
    while x > 0:
        update(particles)
        #render(particles, tick)
        x -= 1
        tick += 1

        if tick == 10117: # magic number: 10117
            print_letters(particles)
            break

# main
ans = sol()
print(ans)
