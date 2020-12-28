def rem(s):

    for i in range(len(s)-1):

        if chr(ord(s[i]) + 32) == s[i+1] or chr(ord(s[i]) - 32) == s[i+1]:
            return s[:i] + s[i+2:]

    return False

def sol():
    data = open("d5.txt").read()[:-1]

    loop = True
    while loop:
        loop = False

        value = rem(data)
        if value != False:
            loop = True
            data = value

    # 48349
    # 10903
    return len(data)


# main
ans = sol()
print(ans)
