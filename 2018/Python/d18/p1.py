import sys

def show(data):
    for row in data:
        print("".join(row))
    print("")

def answer(data):

    trees  = 0
    lumber = 0
    empty  = 0

    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "|":
                trees += 1

            elif data[r][c] == "#":
                lumber += 1

            else: # . empty
                empty += 1

    return trees * lumber

def counts(y, x, data):

    trees  = 0
    lumber = 0
    empty  = 0

    adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for a in adj:
        nx = x + a[0]
        ny = y + a[1]

        if nx < 0 or nx >= len(data[0]) or ny < 0 or ny >= len(data): continue

        if data[ny][nx] == "|":
            trees += 1

        elif data[ny][nx] == "#":
            lumber += 1

        else: # . empty
            empty += 1

    return (trees, lumber, empty)

# advance d1 based on d2
def advance(d1, d2):
    for r in range(len(d1)):
        for c in range(len(d1[0])):
            trees, lumber, empty = counts(r, c, d2)

            print("r,c:", r, c, trees, lumber, empty, d2[r][c])

            d1[r][c] = d2[r][c] # stay the same

            if trees >= 3 and d2[r][c] == ".":
                print("r,c:", r, c, ".", "|")
                d1[r][c] = "|"

            elif lumber >= 3 and d2[r][c] == "|":
                print("r,c:", r, c, "|", "#")
                d1[r][c] = "#"

            elif (lumber == 0 or trees == 0) and d2[r][c] == "#":
                print("r,c:", r, c, "#", ".")
                d1[r][c] = "."

def sol():
    d1 = [list(x.strip()) for x in open("d18.txt").readlines()]
    d2 = [list(x.strip()) for x in open("d18.txt").readlines()]

    show(d1)

    turn = False

    step = 10
    while step > 0:
        if turn:
            advance(d1, d2)
            show(d1)

        else:
            advance(d2, d1)
            show(d2)

        turn = not turn
        step -= 1

    if turn: # turn == True then answer d2
        return answer(d2)

    else:
        return answer(d1)

# main
ans = sol()
print(ans)
# sys.stdout.flush()

# 119680 wrong
