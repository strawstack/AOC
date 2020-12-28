import queue

donut = [x[:-1] for x in open("input.txt").readlines()]

# Letter, or space is a wall
# Dot is floor
# Hashtag is wall

offset = (-1, -1)

# Map from gate name to locations
gateName = {
    "GE": [(3 - 1, 36 - 1), (27 - 1, 68 - 1)],
    "FZ": [(3 - 1, 38 - 1), (83 - 1, 48 - 1)],
    "ZZ": [(3 - 1, 48 - 1), (3 - 1, 48 - 1)],
    "TQ": [(3 - 1, 52 - 1), (50 - 1, 27 - 1)],
    "YI": [(3 - 1, 58 - 1), (62 - 1, 27 - 1)],
    "CT": [(3 - 1, 62 - 1), (83 - 1, 52 - 1)],
    "YX": [(3 - 1, 72 - 1), (38 - 1, 79 - 1)],
    "LI": [(27 - 1, 32 - 1), (74 - 1, 3 - 1)],
    "KL": [(27 - 1, 40 - 1), (42 - 1, 103 - 1)],
    "TX": [(27 - 1, 50 - 1), (107 - 1, 32 - 1)],
    "OK": [(27 - 1, 58 - 1), (107 - 1, 50 - 1)],
    "VY": [(27 - 1, 70 - 1), (56 - 1, 103 - 1)],
    "NA": [(32 - 1, 3 - 1), (83 - 1, 36 - 1)],
    "ZV": [(44 - 1, 3 - 1), (32 - 1, 27 - 1)],
    "YB": [(46 - 1, 3 - 1), (72 - 1, 27 - 1)],
    "LA": [(60 - 1, 3 - 1), (62 - 1, 79 - 1)],
    "PB": [(62 - 1, 3 - 1), (36 - 1, 79 - 1)],
    "HP": [(72 - 1, 3 - 1), (48 - 1, 79 - 1)],
    "HM": [(42 - 1, 27 - 1), (78 - 1, 103 - 1)],
    "GY": [(54 - 1, 27 - 1), (107 - 1, 64 - 1)],
    "XC": [(74 - 1, 27 - 1), (48 - 1, 103 - 1)],
    "QD": [(54 - 1, 79 - 1), (66 - 1, 103 - 1)],
    "UC": [(68 - 1, 79 - 1), (107 - 1, 60 - 1)],
    "XV": [(74 - 1, 79 - 1), (68 - 1, 103 - 1)],
    "EH": [(83 - 1, 42 - 1), (34 - 1, 103 - 1)],
    "XO": [(83 - 1, 58 - 1), (107 - 1, 76 - 1)],
    "TY": [(83 - 1, 62 - 1), (107 - 1, 52 - 1)],
    "TN": [(83 - 1, 74 - 1), (107 - 1, 44 - 1)],
    "AA": [(62 - 1, 103 - 1), (62 - 1, 103 - 1)]
}

# Map from location to gate name
# Computed from gateName
gateLocation = {}
for key in gateName:
    gateLocation[gateName[key][0]] = key
    gateLocation[gateName[key][1]] = key

def getOther(gateName, gateLocation, location):
    name = gateLocation[location]
    if gateName[name][0] == location:
        return gateName[name][1]
    else:
        return gateName[name][0]

def sol(donut, gateName, gateLocation):

    # Init queue
    start = (0, (61, 102)) # steps, location
    q = queue.Queue()
    q.put(start)

    # Track visited
    visited = {}
    visited[start[1]] = True

    # Neighbours
    adj = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while not q.empty():
        steps, location = q.get()

        # Check if we made it to ZZ
        if (location in gateLocation) and gateLocation[location] == "ZZ":
            return steps

        # Step to each neighbor
        for o in adj:
            nr, nc = location[0] + o[0], location[1] + o[1]

            if donut[nr][nc] == ".":
                if (nr, nc) not in visited:
                    q.put( (steps + 1, (nr, nc)) )
                    visited[(nr, nc)] = True

        # Enter teleporter if available
        if location in gateLocation:
            # Location of other side of teleporter
            otherLocation = getOther(gateName, gateLocation, location)
            if otherLocation not in visited:
                q.put( (steps + 1, otherLocation) )
                visited[otherLocation] = True

ans = sol(donut, gateName, gateLocation)
print(ans)
