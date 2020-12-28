#lines = [x[:-1] for x in open("input.txt").readlines()]
moons = [
[4, 1, 1],
[11, -18, -1],
[-2, -10, -4],
[-7, -2, 14]
]

vel = [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
]

def gravity(moons, vel):
    grav = []
    for _ in range(4): grav.append([0 for _ in range(3)])

    # Calculate changes
    for i in range(3):
        for j in range(len(moons)):
            m1 = moons[j]
            for k in range(len(moons)):
                m2 = moons[k]
                if j == k: continue

                if m1[i] < m2[i]:
                    grav[j][i] += 1

                elif m1[i] > m2[i]:
                    grav[j][i] -= 1

    # Apply Gravity
    for j in range(len(vel)):
        for i in range(len(vel[j])):
            vel[j][i] += grav[j][i]

    return None

def velocity(moons, vel):
    for i in range(len(moons)):
        for j in range(len(moons[i])):
            moons[i][j] += vel[i][j]
    return None

def sol():
    for _ in range(1000):
        gravity(moons, vel)
        velocity(moons, vel)

    # Calculate final value
    total = 0
    for i in range(len(moons)):
        pot = abs(moons[i][0]) + abs(moons[i][1]) + abs(moons[i][2])
        kin = abs(vel[i][0]) + abs(vel[i][1]) + abs(vel[i][2])
        total += pot * kin
    return total

ans = sol()
print(ans)
