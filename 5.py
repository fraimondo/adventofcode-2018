import numpy as np
with open('5_in.txt', 'r') as f:
    polymer = f.readline()

def react(t_polymer):
    elems = np.unique(list(t_polymer))
    to_replace = set()
    for elem in elems:
        to_replace.add('{}{}'.format(elem.upper(), elem.lower()))
        to_replace.add('{}{}'.format(elem.lower(), elem.upper()))

    p_len = len(t_polymer)
    n_len = 0
    while n_len != p_len:
        p_len = n_len
        for elem in to_replace:
            t_polymer = t_polymer.replace(elem, '')
        n_len = len(t_polymer)

    return len(t_polymer)

print(react(polymer))

units = set()
elems = np.unique(list(polymer))
for elem in elems:
    units.add(elem.lower())


reactions = {}
for unit in units:
    t_polymer = polymer.replace(
        unit, '').replace(unit.upper(), '')
    reactions[unit] = react(t_polymer)

print(np.min(list(reactions.values())))