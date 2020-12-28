import math

lines = [x[:-1] for x in open("input.txt").readlines()]

# 1 ZJZRN, 4 NZVL, 1 NJFXK, 7 RHJCQ, 32 MCQS, 1 XFNPT => 5 ZWQX

def possibleGain(reaction, over):
    for key in over:
        if key not in reaction: continue
        f = math.floor(over[key] / reaction[key][0])
        if f > 0:
            return key, f
    return False, False

def reverseExchange(reaction, over):
    # Change access chemical back into ORE
    while True:

        # As long as there is enough chemical to
        # fire one reaction
        key, factor = possibleGain(reaction, over)
        if key == False: break

        # Remove exchange chemical
        over[key] -= reaction[key][0] * factor

        # Add created chemicals to over
        for qty, type in reaction[key][1]:
            if type not in over: over[type] = 0
            over[type] += qty * factor

    return over["ORE"]

def requiredOre(reaction, type, qty, over):
    if type == "ORE": return qty

    ore = 0

    # Amount of chemical this rule outputs
    _out_qty = reaction[type][0]

    # Number of times you have to run this reaction
    # to make at least what you need
    factor = math.ceil(qty / _out_qty)

    for _input in reaction[type][1]:
        _qty, _type = _input
        ore += requiredOre(reaction, _type, _qty * factor, over)

    if (factor * _out_qty) > qty:
        if type not in over:
            over[type] = 0
        over[type] += (factor * _out_qty) - qty
    return ore

def sol():
    over = {}
    # Map output_type -> [qty, input_list]
    reaction = {}

    for line in lines:
        r_in, r_out = line.split("=>")
        r_input_list = [x.strip().split(" ") for x in r_in.split(",")]

        # List of tuples of type (qty, type)
        r_input_list = list(map(lambda x: (int(x[0]), x[1]), r_input_list))
        r_out = r_out.strip().split(" ")

        # Single tuple (qty, type)
        r_out[0] = int(r_out[0])

        reaction[r_out[1]] = [r_out[0], r_input_list]

    value = requiredOre(reaction, "FUEL", 1, over)
    gain = reverseExchange(reaction, over)

    return value - gain

ans = sol()
print(ans)
