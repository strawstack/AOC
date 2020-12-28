grid = [x[:-1] for x in open("input.txt").readlines()]
grid = list(map(lambda row: list(row), grid))

# Note: all characters other than '#' and '.' are
# a-z, A-Z or @

def sol():
    ROW_COUNT = len(grid)
    COL_COUNT = len(grid[0])
    letterLocation = getLetterLocations(grid)

    # Call BFS on start location

    # Hide @ symbol (location is stored in 'letterLocation')
    start = letterLocation["@"]
    grid[start["row"]][start["col"]] = "."

    edgeList = {}

    for key in letterLocation:
        if (key == "@"): continue
        edgeList[key] = bfs(grid, letterLocation[key])

    # print(letterLocation)
    print(edgeList)

# Return map {letter -> {row:, col:}}
def getLetterLocations(grid):
    ROW_COUNT = len(grid)
    COL_COUNT = len(grid[0])
    letterLocation = {}
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            letter = grid[r][c]
            if isLetter(letter):
                letterLocation[letter] = {
                    "row": r, "col": c
                }
    return letterLocation

# Return reachable symbols from given location
def bfs(grid, loc):
    ROW_COUNT = len(grid)
    COL_COUNT = len(grid[0])
    q = [{"steps": 0, "loc": loc}]
    visited = {}

    destination = {}

    while len(q) > 0:
        cur = q.pop(0)
        h = hash(cur["loc"])
        visited[h] = True

        adj = [
            {"row": -1, "col": 0}, {"row": 1, "col": 0},
            {"row": 0, "col": -1}, {"row": 0, "col": 1}
        ]

        for offset in adj:
            move = {
                "row": cur["loc"]["row"] + offset["row"],
                "col": cur["loc"]["col"] + offset["col"]
            }
            if bounds(ROW_COUNT, COL_COUNT, grid, move):
                if hash(move) not in visited:
                    letter = grid[move["row"]][move["col"]]
                    if isLetter(letter):
                        destination[letter] = cur["steps"] + 1
                    else:
                        q.append({
                            "steps": cur["steps"] + 1,
                            "loc": move
                        })

    return destination

def hash(loc):
    return str(loc["row"]) + ":" + str(loc["col"])

def bounds(ROW_COUNT, COL_COUNT, grid, move):
    r = move["row"]
    c = move["col"]
    rowCheck = r >= 0 and r < ROW_COUNT
    colCheck = c >= 0 and c < COL_COUNT
    isWall = grid[move["row"]][move["col"]] == "#"
    return rowCheck and colCheck and (not isWall)

def isLetter(letter):
    return (not (letter == "#")) and (not (letter == "."))

# main
ans = sol()
print(ans)
