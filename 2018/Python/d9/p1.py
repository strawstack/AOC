import sys

def sol():
    # 491 players; last marble is worth 71058 points
    # data = [x.strip() for x in open("d9.txt").readlines()]

    #if False:
    p = 491
    s = 71058

    # test
    #p = 10
    #s = 1618

    marble = 2
    circle = [0, 1]
    player = 1
    score = [0 for x in range(p)]
    index = 1

    while True:

        #print(circle)
        sys.stdout.flush()

        # special
        if marble % 23 == 0:
            back = (index - 7) % len(circle)
            rem = circle.pop(back)
            total_score = marble + rem
            # print("total_score:", total_score)
            sys.stdout.flush()
            score[player] += total_score

            # update current
            index = back

        else:
            # insert marble and update index
            #print("player", player + 1, "places", marble )
            nx_index = (index + 2) % len(circle)
            circle.insert(nx_index, marble)
            index = nx_index

        # end condition
        if marble == s: return max(score)

        marble += 1
        player = (player + 1) % p



# main
ans = sol()
print(ans)


# 8317
