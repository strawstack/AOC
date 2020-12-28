import sys

def get(dict, pos):
    if not pos in dict: return "."
    return dict[pos]

def total(state):
    t = 0
    # print(state)
    for k in state:
        if state[k] == "#":
            t += k
    return t

def advance(state, rules):
    newstate = {}

    # track outer values to see if plants
    # should spawn out there
    low = float("inf")
    high = float("-inf")

    for s in state:
        low  = min(low, s)
        high = max(high, s)

    #print("low:", low)
    #print("high:", high)
    for s in range(low - 2, high + 2 + 1):
        local = ""
        for i in range(-2, 2+1):
            local += get(state, s + i)

        for rule in rules:
            if local == rule[0]:
                newstate[s] = rule[1]

    return newstate

def sol():
    data = [x.strip() for x in open("d12.txt").readlines()]

    initial = data[0].split(": ")[1]
    state = {}
    for i in range(len(initial)):
        state[i] = initial[i]

    #print(initial)

    rules = data[2:]
    for i in range(len(rules)):
        rules[i] = [x for x in rules[i].split(" => ")]

    #print(rules)

    for j in range(20):
        state = advance(state, rules)

    #print(state)
    return total(state)

# main
ans = sol()
print(ans)
# sys.stdout.flush()

# 2268 too low
# 3294 too high
