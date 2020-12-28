import sys

FIFTY_BILLION = 50000000000

def get(dict, pos):
    if not pos in dict: return "."
    return dict[pos]

def hash(dict):
    low = float("inf")
    high = float("-inf")
    for s in dict:
        low  = min(low, s)
        high = max(high, s)

    h = ""
    for i in range(low, high+1):
        h += get(dict, i)
    return h

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
    seen = {}
    seen[hash(state)] = -1 # gen -1 is initial

    score = [0]
    for j in range(300):

        mytotal = total(state)
        print("total:", mytotal, "gen:", j, "diff:", mytotal - score[j])
        score.append(mytotal)
        sys.stdout.flush()
        state = advance(state, rules)

    #print(state)
    return total(state)

# main
ans = sol()
print(ans)
# sys.stdout.flush()

# equation
# total: 13713, gen: 168
# 13713 + (50000000000 - 168) * 75 = 3750000001113
