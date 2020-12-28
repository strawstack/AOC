import sys

NUM_UNITS   = 0
HIT_POINT   = 1
WEAK        = 2
IMMUNE      = 3
ATTACK_DMG  = 4
ATTACK_TYPE = 5
INITIATIVE  = 6
GROUP_TYPE  = 7
TARGET      = 8
ID          = 9

D = False
D1 = False

# num units multiplied by attack damage
def effective_power(group):
    return group[NUM_UNITS] * group[ATTACK_DMG]

def copy(group):
    return [
        group[NUM_UNITS],
        group[HIT_POINT],
        group[WEAK][:],
        group[IMMUNE][:],
        group[ATTACK_DMG],
        group[ATTACK_TYPE],
        group[INITIATIVE],
        group[GROUP_TYPE],
        group[TARGET],
        group[ID]
    ]

def copy_groups(groups):
    rtn = []
    for g in groups:
        rtn.append(copy(g))
    return rtn

def pos_damage(attacker, group):
    if attacker[ATTACK_TYPE] in group[IMMUNE]:
        return 0 # no damage if immune

    mult = 2 if (attacker[ATTACK_TYPE] in group[WEAK]) else 1
    damage_done = mult * effective_power(attacker)

    return damage_done

# choose enemy that takes the most damage
# and break ties by larger effective power
# and higher initiative
# returns: array index of group to attack this round
def target_selection(attacker, groups, attack):
    cgroups = copy_groups(groups[:])
    cgroups = sorted(cgroups, key=lambda g: (-1 * pos_damage(attacker, g), -1 * effective_power(g), -1 * g[INITIATIVE]))

    for g in cgroups:
        # Infection group 1 would deal defending group 1 185832 damage
        if attacker[ID] != g[ID] and attacker[GROUP_TYPE] != g[GROUP_TYPE] and (not g[ID] in attack):
            return g[ID]

    return None

def attack_order(all_groups):
    return sorted(all_groups, key=lambda g: -1 * g[INITIATIVE])

def sort_one(g):
    return (-1 * effective_power(g), -1 * g[INITIATIVE])

def target_order(all_groups):
    return list(sorted(all_groups, key=lambda g: sort_one(g)))

def perform_attack(i, all_groups):
    target_id = all_groups[i][TARGET]
    if target_id == None: return None # attacker did not select a target
    if all_groups[i][NUM_UNITS] <= 0: return None # attacker no units, it can't attack

    for g in range(len(all_groups)):
        if all_groups[i][TARGET] == all_groups[g][ID]:

            # perform attack
            if all_groups[i][ATTACK_TYPE] in all_groups[g][IMMUNE]:
                return None # no damage if immune

            mult = 2 if (all_groups[i][ATTACK_TYPE] in all_groups[g][WEAK]) else 1
            damage_done = mult * effective_power(all_groups[i])
            units_lost = damage_done // all_groups[g][HIT_POINT]

            if D: print(" ", all_groups[i][ID], "attacks", all_groups[g][ID], "killing", units_lost, "units")
            #if D: print("--", attacker)
            #if D: print("--", group)

            # kill enemy units
            all_groups[g][NUM_UNITS] -= units_lost
            #if D: print("  group", group[ID], "now has", group[NUM_UNITS], "units")
            return None

def num_units(all_groups):
    total_immune_group    = 0
    total_infection_group = 0

    for g in all_groups:
        if g[GROUP_TYPE]:
            if g[NUM_UNITS] > 0:
                total_immune_group += g[NUM_UNITS]

        else:
            if g[NUM_UNITS] > 0:
                total_infection_group += g[NUM_UNITS]

    return total_immune_group, total_infection_group

def num_units2(all_groups):
    total_immune_group    = []
    total_infection_group = []

    for g in all_groups:
        if g[GROUP_TYPE]:
            total_immune_group.append(g[NUM_UNITS])

        else:
            total_infection_group.append(g[NUM_UNITS])

    return total_immune_group, total_infection_group

# True if should keep going
# False is war is over
def end_condition(all_groups):
    total_immune_group, total_infection_group = num_units(all_groups)
    return (total_immune_group > 0) and (total_infection_group > 0)

def sol():
    immune_group = [
        [3609, 2185, ["cold", "radiation"], [], 5, "slashing", 20, True, None, 0],
        [72, 5294, ["slashing"], ["radiation", "cold"], 639, "fire", 1, True, None, 1],
        [4713, 6987, ["radiation"], [], 12, "slashing", 2, True, None, 2],
        [623, 9745, [], [], 137, "cold", 6, True, None, 3],
        [1412, 9165, [], [], 52, "bludgeoning", 3, True, None, 4],
        [2042, 7230, [], ["cold", "radiation"],25, "bludgeoning", 15, True, None, 5],
        [209, 9954, [], [], 384, "cold", 17, True, None, 6],
        [33, 6495, ["fire"], [], 1756, "fire", 7, True, None, 7],
        [242, 6650, [], ["radiation", "fire"], 239, "bludgeoning", 12, True, None, 8],
        [4701, 7384, [], ["cold"], 14, "fire", 9, True, None, 9]
    ]

    infection_group = [
        [4154, 21287, [], ["fire", "slashing", "cold", "radiation"], 9, "fire", 5, False, None, 10],
        [2091, 5531, [], ["slashing"], 5, "fire", 13, False, None, 11],
        [2237, 24000, [], [], 20, "fire", 16, False, None, 12],
        [149, 31282, ["radiation", "cold"], [], 329, "radiation", 8, False, None, 13],
        [649, 39642, [], [], 108, "cold", 18, False, None, 14],
        [108, 35626, ["slashing"], ["radiation"], 519, "cold", 4, False, None, 15],
        [1194, 37567, ["fire", "radiation"], [], 59, "radiation", 19, False, None, 16],
        [2849, 37603, [], ["cold"], 26, "bludgeoning", 10, False, None, 17],
        [451, 35892, ["slashing"], ["cold"], 133, "fire", 14, False, None, 18],
        [3232, 27332, ["fire"], [], 14, "cold", 11, False, None, 19]
    ]

    test_immune_group =[
        [17, 5390, ["radiation", "bludgeoning"], [], 4507, "fire", 2, True, None, "IM_1"],
        [989, 1274, ["bludgeoning", "slashing"], ["fire"], 25, "slashing", 3, True, None, "IM_2"]
    ]

    test_infection_group = [
        [801, 4706, ["radiation"], [], 116, "bludgeoning", 1, False, None, "INF_1"],
        [4485, 2961, ["fire"], ["radiation"], 12, "slashing", 4, False, None, "INF_2"]
    ]

    all_groups = immune_group + infection_group
    #all_groups = test_immune_group + test_infection_group

    while end_condition(all_groups):

        if D: print("num_units:", num_units2(all_groups))

        # target selection
        all_groups = target_order(all_groups)

        #if D1: print("show target order")
        #for g in all_groups:
        #    print(g)

        attack = {}
        for attacker in all_groups:
            target_id = target_selection(attacker, all_groups, attack)
            attack[target_id] = True
            attacker[TARGET] = target_id

        # attacking
        all_groups = attack_order(all_groups)

        for i in range(len(all_groups)):
            perform_attack(i, all_groups)

        # remove dead groups
        all_groups = list(filter(lambda x: x[NUM_UNITS] > 0, all_groups))

        if D: print("num_units:", num_units(all_groups))
        if D: print("end condition:", end_condition(all_groups))

    return num_units(all_groups)

# main
a, b = sol()
print(a, b)
# sys.stdout.flush()

# 10535 too low
# 15502 too high
# 13018 too low
# 14260 wrong (no info)
# 15495 wrong (no info)
# 15493
