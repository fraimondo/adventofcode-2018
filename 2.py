import numpy as np
from collections import Counter
with_2 = 0
with_3 = 0

ids = []

with open('2_in.txt', 'r') as f:
    for line in f:
        ids.append(line.strip())
        counts = Counter(line)
        if 3 in counts.values():
            with_3 += 1
        if 2 in counts.values():
            with_2 += 1

print(with_2 * with_3)

def distance(a, b):
    return np.sum(np.array([a[i] != b[i] for i in range(len(a))]))

st = 0
found = False
while st < len(ids) and found is False:
    t = st + 1
    while t < len(ids) and found is False:
        if distance(ids[st], ids[t]) == 1:
            print('found')
            found = True
        t += 1
    st += 1

a = ids[st - 1]
b = ids[t - 1]
print(a)
print(b)
print(''.join([a[i] for i in range(len(a)) if a[i] == b[i]]))
