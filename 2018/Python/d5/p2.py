import sys

def sol(data, one, two):

    data = data.replace(one, "")
    data = data.replace(two, "")

    stack = []
    for c in data:
        if len(stack) == 0:
            stack.append(c)
            continue

        ct = stack.pop()
 
        if chr(ord(ct) + 32) == c or chr(ord(ct) - 32) == c:
            pass
        else:
            stack.append(ct)
            stack.append(c)

    return len(stack)

# main
data = open("d5.txt").read()[:-1]
ans = []
for i in range(26): ans.append(sol(data[:], chr(i + 65), chr(i + 97)))
print(min(ans))
