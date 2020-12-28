import sys
sys.setrecursionlimit(10000)

success_log = {}
DOWN  = 0
LEFT  = 1
RIGHT = 2

def hash(x,y):
    return str(x) + ":" + str(y)

def draw_map(clay, visited):
    for row in range(0, 1856 + 10):
        for col in range(259 - 10, 685 + 10):
            h = hash(row, col)
            if h in clay:
                print("#", end="")
            elif h in visited:
                print("~", end="")
            else:
                print(".", end="")
        print("")
    print("")

# make the surface absorb until
# prev upstream
def rip(y, x, visited):

    while not hash(y - 1, x) in visited:
        success_log[hash(y, x)] = True
        x += 1


# preform DFS from given node
# return true if end reached
# return false if blocked
def dfs(n, clay, visited, min_max, success, parent, phash): # parent: DOWN, LEFT, RIGHT
    y, x = n
    visited[hash(y, x)] = (y, x)
    if success: success_log[hash(y, x)] = True
    #draw_map(clay, visited)

    chash = None

    # down
    h = hash(y + 1, x)

    # the guy below you will adsorb and above you is
    # water indicating that you're falling
    if h in success_log and hash(y - 1, x) in visited:
        return True

    if not h in clay and not h in visited:
        success = False
        if (y + 1) > min_max[1]: return True

        if parent == LEFT:
            rip(y, x, visited)

        chash = h
        end = dfs((y + 1, x), clay, visited, min_max, False, DOWN, hash(y,x))
        if end: return end

    # right
    right_success = False
    h = hash(y, x + 1)
    if not h in clay and not h in visited:
        success = False
        chash = h
        right_success = dfs((y, x + 1), clay, visited, min_max, False, RIGHT, hash(y,x))

    if h in visited and h != phash and h != chash:
        return True

    # left
    h = hash(y, x - 1)
    if not h in clay and not h in visited:
        end = dfs((y, x - 1), clay, visited, min_max, right_success | success, LEFT, hash(y,x))
        return right_success | end

    return right_success

def sol():
    data = [x.strip() for x in open("d17.txt").readlines()]

    min_max = [float("inf"), float("-inf")]

    clay = {}
    for row in data:
        # x=442, y=708..721
        one, two = row.split(", ")
        a, b = one.split("=") # a = x
        b = int(b) # b = 442

        c, d = two.split("=") # c = y
        e, f = [int(g) for g in d.split("..")] # e = 708, f = 721

        if a == "x":
            min_max = [min(min_max[0], e, f), max(min_max[1], e, f)]
            for i in range(e, f + 1):
                clay[hash(i, b)] = True

        else: # a == "y"
            min_max = [min(min_max[0], b), max(min_max[1], b)]
            for i in range(e, f + 1):
                clay[hash(b, i)] = True

    # 1. walk down, until you hit clay
    # 2. move left and right until there is nothing below
    # 3. step back up the stream
    # 4. repeat step 1

    visited = {}
    _ = dfs((0, 500), clay, visited, min_max, False, DOWN, hash(0, 500))

    draw_map(clay, visited)

    cxmin, cxmax = float("inf"), float("-inf")

    total = 0
    for k in visited:
        y, x = visited[k]
        cxmin, cxmax = min(cxmin, x), max(cxmax, x)
        if y >= min_max[0]:
            total += 1

    print(min_max[0], min_max[1])
    print(cxmin, cxmax)
    return total

# main
ans = sol()
print(ans)
# sys.stdout.flush()

# 44153 wrong
# 3681336 wrong
# 3679302 wrong
# 98586 wrong
# 94404 wrong
# 3679243 wrong
# 46340 wrong
# 54051 wrong
# 52860 wrong
