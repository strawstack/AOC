def differ(w1, w2):

    diff = 0
    index = -1

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
            index = i

    if diff == 1:
        return index

    return False


def sol():
    data = [x.strip() for x in open("d2.txt").readlines()]

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            index = differ(data[i], data[j])

            if index != False:
                # the answer is data[i] with index removed
                return data[i], index # lujnogabetpmsydyfcovzixaw

# main
ans = sol()
print(ans)
