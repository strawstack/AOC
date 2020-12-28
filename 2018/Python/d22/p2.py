import sys
import heapq

ROCKY  = 0
WET    = 1
NARROW = 2

GEAR    = 3
TORCH   = 4
NEITHER = 5

class State:
    def __init__(self, r, c, cost, tool):
        self.r = r
        self.c = c
        self.cost = cost
        self.tool = tool
        self.hash = (r, c, tool)

    def __lt__(self, other):
        return self.cost < other.cost

def dijkstras(cave, tr, tc, erosion_levels, depth):

    s = State(0, 0, 0, TORCH)
    q = [(0, s)]

    dist = {}
    dist[s.hash] = 0

    parent = {}
    parent[s.hash] = None

    visited = {}
    while len(q) != 0:

        cost, cur = heapq.heappop(q)

        # end condition
        if cur.r == tr and cur.c == tc:
            has_torch = 0 if cur.tool == TORCH else 7
            return cur.cost + has_torch, parent, cur

        visited[cur.hash] = True

        # update the distances to each reachable child
        # that has not already been visited
        for off in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cur.r + off[0], cur.c + off[1]

            if nr < 0 or nc < 0: continue

            h = hash(nr, nc)
            if not h in cave:
                cave[h] = getRType(nr, nc, erosion_levels, depth, cave, tr, tc)

            change_move = 7 + 1
            move_time   = 1

            r_type = cave[h]
            if r_type == ROCKY:
                if cur.tool == GEAR or cur.tool == TORCH:
                    child_state = State(nr, nc, cur.cost + 1, cur.tool)
                    if child_state.hash in visited: continue

                    if not child_state.hash in dist:
                        dist[child_state.hash] = cur.cost + 1
                        parent[child_state.hash] = cur
                        heapq.heappush(q, (cur.cost + 1, child_state))
                    else:
                        if cur.cost + 1 < dist[child_state.hash]:
                            dist[child_state.hash] = cur.cost + 1
                            parent[child_state.hash] = cur
                            heapq.heappush(q, (cur.cost + 1, child_state))

                else: # cur.tool == NEITHER
                    child_state  = State(nr, nc, cur.cost + change_move, GEAR)
                    child_state2 = State(nr, nc, cur.cost + change_move, TORCH)
                    if child_state.hash in visited: continue
                    if child_state2.hash in visited: continue

                    if not child_state.hash in dist:
                        dist[child_state.hash] = cur.cost + change_move
                        parent[child_state.hash] = cur
                        heapq.heappush(q, (cur.cost + change_move, child_state))
                    else:
                        if cur.cost + change_move < dist[child_state.hash]:
                            dist[child_state.hash] = cur.cost + change_move
                            parent[child_state.hash] = cur
                            heapq.heappush(q, (cur.cost + change_move, child_state))

                    if not child_state2.hash in dist:
                        dist[child_state2.hash] = cur.cost + change_move
                        parent[child_state2.hash] = cur
                        heapq.heappush(q, (cur.cost + change_move, child_state2))
                    else:
                        if cur.cost + change_move < dist[child_state2.hash]:
                            dist[child_state2.hash] = cur.cost + change_move
                            parent[child_state2.hash] = cur
                            heapq.heappush(q, (cur.cost + change_move, child_state2))

            elif r_type == WET:
                if cur.tool == GEAR or cur.tool == NEITHER:
                    child_state = State(nr, nc, cur.cost + 1, cur.tool)
                    if child_state.hash in visited: continue

                    if not child_state.hash in dist:
                        dist[child_state.hash] = cur.cost + 1
                        parent[child_state.hash] = cur
                        heapq.heappush(q, (cur.cost + 1, child_state))
                    else:
                        if cur.cost + 1 < dist[child_state.hash]:
                            dist[child_state.hash] = cur.cost + 1
                            parent[child_state.hash] = cur
                            heapq.heappush(q, (cur.cost + 1, child_state))

                else: # cur.tool == TORCH
                    child_state  = State(nr, nc, cur.cost + change_move, GEAR)
                    child_state2 = State(nr, nc, cur.cost + change_move, NEITHER)
                    if child_state.hash in visited: continue
                    if child_state2.hash in visited: continue

                    if not child_state.hash in dist:
                        dist[child_state.hash] = cur.cost + change_move
                        parent[child_state.hash] = cur
                        heapq.heappush(q, (cur.cost + change_move, child_state))
                    else:
                        if cur.cost + change_move < dist[child_state.hash]:
                            dist[child_state.hash] = cur.cost + change_move
                            parent[child_state.hash] = cur
                            heapq.heappush(q, (cur.cost + change_move, child_state))

                    if not child_state2.hash in dist:
                        dist[child_state2.hash] = cur.cost + change_move
                        parent[child_state2.hash] = cur
                        heapq.heappush(q, (cur.cost + change_move, child_state2))
                    else:
                        if cur.cost + change_move < dist[child_state2.hash]:
                            dist[child_state2.hash] = cur.cost + change_move
                            parent[child_state2.hash] = cur
                            heapq.heappush(q, (cur.cost + change_move, child_state2))

            else: # r_type == NARROW
                if cur.tool == TORCH or cur.tool == NEITHER:
                    child_state = State(nr, nc, cur.cost + 1, cur.tool)
                    if child_state.hash in visited: continue

                    if not child_state.hash in dist:
                        dist[child_state.hash] = cur.cost + 1
                        parent[child_state.hash] = cur
                        heapq.heappush(q, (cur.cost + 1, child_state))
                    else:
                        if cur.cost + 1 < dist[child_state.hash]:
                            dist[child_state.hash] = cur.cost + 1
                            parent[child_state.hash] = cur
                            heapq.heappush(q, (cur.cost + 1, child_state))

                else: # cur.tool == GEAR
                    child_state  = State(nr, nc, cur.cost + change_move, TORCH)
                    child_state2 = State(nr, nc, cur.cost + change_move, NEITHER)
                    if child_state.hash in visited: continue
                    if child_state2.hash in visited: continue

                    if not child_state.hash in dist:
                        dist[child_state.hash] = cur.cost + change_move
                        parent[child_state.hash] = cur
                        heapq.heappush(q, (cur.cost + change_move, child_state))
                    else:
                        if cur.cost + change_move < dist[child_state.hash]:
                            dist[child_state.hash] = cur.cost + change_move
                            parent[child_state.hash] = cur
                            heapq.heappush(q, (cur.cost + change_move, child_state))

                    if not child_state2.hash in dist:
                        dist[child_state2.hash] = cur.cost + change_move
                        parent[child_state2.hash] = cur
                        heapq.heappush(q, (cur.cost + change_move, child_state2))
                    else:
                        if cur.cost + change_move < dist[child_state2.hash]:
                            dist[child_state2.hash] = cur.cost + change_move
                            parent[child_state2.hash] = cur
                            heapq.heappush(q, (cur.cost + change_move, child_state2))

def hash(r, c):
    return (r, c)

def getRType(r, c, erosion_levels, depth, cave, tr, tc):
    up   = hash(r - 1, c)
    left = hash(r, c - 1)

    if not up in cave:
        # calc all up from the top
        for row in range(0, r):
            geo_index = getGeologicIndex(row, c, erosion_levels, tr, tc)
            erosion_level = getErosionLevel(geo_index, depth, 20183)
            erosion_levels[hash(row, c)] = erosion_level
            r_type = getType(erosion_level)
            cave[hash(row, c)] = r_type

    if not left in cave:
        # calc all left from side
        for col in range(0, c):
            geo_index = getGeologicIndex(r, col, erosion_levels, tr, tc)
            erosion_level = getErosionLevel(geo_index, depth, 20183)
            erosion_levels[hash(r, col)] = erosion_level
            r_type = getType(erosion_level)
            cave[hash(r, col)] = r_type

    geo_index = getGeologicIndex(r, c, erosion_levels, tr, tc)
    erosion_level = getErosionLevel(geo_index, depth, 20183)
    erosion_levels[hash(r, c)] = erosion_level
    r_type = getType(erosion_level)

    return r_type

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
    size = 70
    for r in range(0, tr + 1):
        for c in range(0, tc + 1):

            geo_index = getGeologicIndex(r, c, erosion_levels, tr, tc)
            erosion_level = getErosionLevel(geo_index, depth, 20183)
            erosion_levels[hash(r, c)] = erosion_level
            r_type = getType(erosion_level)

            cave[hash(r, c)] = r_type

    print("call dijkstras")
    sys.stdout.flush()
    ans, parent, ts = dijkstras(cave, tr, tc, erosion_levels, depth)

    # print path
    if False:
        print(ts.r, ts.c, ts.tool, ts.cost)
        nx = parent[ts.hash]
        while nx != None:
            print(nx.r, nx.c, nx.tool, nx.cost)
            nx = parent[nx.hash]

    return ans

# main
ans = sol()
print(ans)
# sys.stdout.flush()

# 1090 too low
# 1097 too high
# 1094 too high
# 1092 correct!
