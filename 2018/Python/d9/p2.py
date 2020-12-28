import sys

class Node:
    def __init__(self, value, prev, next):
        self.prev = prev
        self.next = next
        self.value = value

    def __str__(self):
        return str(self.prev.value) + " (" + str(self.value) + ") " + str(self.next.value)

def linked_pop(cur):
    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    return cur.value

def add_before(new, cur):
    new.prev = cur.prev
    new.prev.next = new
    new.next = cur
    cur.prev = new
    return new

def sol():
    # 491 players; last marble is worth 71058 points
    # data = [x.strip() for x in open("d9.txt").readlines()]

    #if False:
    p = 491
    s = 71058 * 100

    # test
    #p = 10
    #s = 1618

    marble = 2
    zero = Node(0, None, None)
    one  = Node(1, zero, zero)
    zero.prev = one
    zero.next = one

    # circle = [0, 1]
    player = 1
    score = [0 for x in range(p)]
    cur = one

    while True:

        #print(cur)
        if marble % 10000 == 0:
            print(marble)
            sys.stdout.flush()

        # special
        if marble % 23 == 0:
            for _ in range(7): cur = cur.prev
            temp = cur.next
            rem = linked_pop(cur)
            cur = temp
            total_score = marble + rem
            score[player] += total_score

        else:
            for _ in range(2): cur = cur.next
            cur = add_before(Node(marble, None, None), cur)

        # end condition
        if marble == s: return max(score)

        marble += 1
        player = (player + 1) % p



# main
ans = sol()
print(ans)


# 8317
