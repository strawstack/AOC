def sol():
    data = [x.strip() for x in open("d2.txt").readlines()]

    two   = 0
    three = 0

    for word in data:

        temp = {}
        for c in word:
            if not c in temp: temp[c] = 0
            temp[c] += 1

        for k in temp:
            if temp[k] == 2:
                two += 1
                break

        for k in temp:
            if temp[k] == 3:
                three += 1
                break

    return two * three



# main
ans = sol()
print(ans)
