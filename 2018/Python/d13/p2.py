import sys

# add one right turn, subtract one for left turn
L = 0
U = 1
R = 2
D = 3

F = -1

# track
# | \ + - /

class Cart:
    def __init__(self, x, y, facing, track, id):
        self.x = x
        self.y = y
        self.facing = facing
        self.track = track
        self.id = id
        if self.id == F: print("loc:", self.y, self.x)
        self.turns = [-1, 0, 1]
        self.turn = 0
        self.status = True

    def move(self): # move one space forward
        # print("coord:", self.y, self.x)
        if self.id == F: print("moves: ", end="")

        if self.facing == L:
            if self.id == F: print("left")
            self.x -= 1

        elif self.facing == R:
            if self.id == F: print("right")
            self.x += 1

        elif self.facing == U:
            if self.id == F: print("up")
            self.y -= 1

        elif self.facing == D:
            if self.id == F: print("down")
            self.y += 1
        if self.id == F: print("loc:", self.y, self.x)

    def nx_facing(self):
        self.facing = (self.facing + self.turns[self.turn]) % 4
        self.turn = (self.turn + 1) % 3
        return self.facing

    def piece(self):
        if self.id == F: print("piece:", self.track[self.y][self.x])
        return self.track[self.y][self.x]

    def react(self): # react the the track you are currently on

        p = self.piece()

        if p == "/" and self.facing == D:
            self.facing = L

        elif p == "/" and self.facing == U:
            self.facing = R

        elif p == "/" and self.facing == L:
            self.facing = D

        elif p == "/" and self.facing == R:
            self.facing = U

        elif p == "\\" and self.facing == D:
            self.facing = R

        elif p == "\\" and self.facing == U:
            self.facing = L

        elif p == "\\" and self.facing == L:
            self.facing = U

        elif p == "\\" and self.facing == R:
            self.facing = D

        elif p == "+":
            self.facing = self.nx_facing()

def check_for_collisions(movecart, carts):
    for cart in carts:
        if not cart.status: continue
        if cart.id == movecart.id: continue

        if cart.x == movecart.x and cart.y == movecart.y:
            cart.status = False
            movecart.status = False
            return True

    return False

def render(carts, track):

    new_track = [x[:] for x in track]

    for cart in carts:
        face = {
            U: "^",
            D: "v",
            L: "<",
            R: ">"
        }
        new_track[cart.y][cart.x] = face[cart.facing]

    for y in range(len(new_track)):
        for x in range(len(new_track[y])):
            print(new_track[y][x], end="")
        print("")
    print("")

def sol():
    track = [list(x.rstrip()) for x in open("d13.txt").readlines()]

    # get carts
    # the piece under them is pointing the same way as them
    carts = []
    id = 0
    for y, row in enumerate(track):
        for x, col in enumerate(row):
            if track[y][x] == "<":
                carts.append( Cart(x, y, L, track, id) )
                id += 1
                track[y][x] = "-"

            elif track[y][x] == ">":
                carts.append( Cart(x, y, R, track, id) )
                id += 1
                track[y][x] = "-"

            elif track[y][x] == "^":
                carts.append( Cart(x, y, U, track, id) )
                id += 1
                track[y][x] = "|"

            elif track[y][x] == "v":
                carts.append( Cart(x, y, D, track, id) )
                id += 1
                track[y][x] = "|"

    # initial
    #render(carts, track)

    step = 0
    hit = False
    while True:
        carts = sorted(carts, key=lambda c: (c.y, c.x))
        for cart in carts:
            if not cart.status: continue

            cart.move()

            #render(carts, track)

            hit = check_for_collisions(cart, carts)
            if hit:
                print("crash")
                sys.stdout.flush()

            cart.react()

        # remove crashed cars
        carts = list(filter(lambda x: x.status, carts))

        if len(carts) == 1:
            print(" step:", step, "location:", carts[0].x, carts[0].y)
            sys.stdout.flush()
            break

        step += 1


# main
ans = sol()
print(ans)
# sys.stdout.flush()

# 72,22 wrong
# 22,72 wrong
