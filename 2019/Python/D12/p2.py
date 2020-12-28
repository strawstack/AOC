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

def velocity(moons, vel, x_states, y_states, z_states, timestep):
    for i in range(len(moons)):
        for j in range(len(moons[i])):
            moons[i][j] += vel[i][j]

    state_x = (moons[0][0], moons[1][0], moons[2][0], moons[3][0], vel[0][0], vel[1][0], vel[2][0], vel[3][0])
    state_y = (moons[0][1], moons[1][1], moons[2][1], moons[3][1], vel[0][1], vel[1][1], vel[2][1], vel[3][1])
    state_z = (moons[0][2], moons[1][2], moons[2][2], moons[3][2], vel[0][2], vel[1][2], vel[2][2], vel[3][2])

    x_value = False
    y_value = False
    z_value = False

    if state_x in x_states:
        x_value = True
    else:
        x_states[state_x] = timestep

    if state_y in y_states:
        y_value = True
    else:
        y_states[state_y] = timestep

    if state_z in z_states:
        z_value = True
    else:
        z_states[state_z] = timestep

    return x_value, y_value, z_value

def sol():

    # Map (State -> timestep of first occurance)
    x_states = {}
    x_states[(4, 11, -2, -7, 0, 0, 0, 0)] = 0
    y_states = {}
    y_states[(1, -18, -10, -2, 0, 0, 0, 0)] = 0
    z_states = {}
    z_states[(1, -1, -4, 14, 0, 0, 0, 0)] = 0

    # Time for complete loop
    xt, yt, zt = 0, 0, 0

    timestep = 0
    x, y, z = False, False, False
    while not (x and y and z):
        timestep += 1

        # Advance by one state
        gravity(moons, vel)

        # Returns true if a coordinate
        x, y, z = velocity(moons, vel, x_states, y_states, z_states, timestep)

        # Grab the time of a complete loop
        if x and xt == 0: xt = timestep
        if y and yt == 0: yt = timestep
        if z and zt == 0: zt = timestep

    # Find the lowest LCM of any x,y,z combo
    print(xt, yt, zt)
    print(len(x_states), len(y_states), len(z_states))

    # NOTE: it might help to look at the values
    # to see the size of the search space


    return None

ans = sol()
print(ans)
