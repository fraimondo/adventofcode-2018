import numpy as np
count = 0
with open('1_in.txt', 'r') as f:
    for line in f:
        count += int(line)
print(count)

origelems = []
with open('1_in.txt', 'r') as f:
    for line in f:
        origelems.append(int(line))

elems = [x for x in origelems]

sums = np.cumsum(elems)
it = 0
while np.unique(sums).shape[0] == len(elems):
    elems += origelems
    sums = np.cumsum(elems)
    it += 1

elems = []
for i in range(it):
    elems += origelems

for t in range(len(origelems)):
    elems.append(origelems[t])
    sums = np.cumsum(elems)
    if np.unique(sums).shape[0] != len(elems):
        print(sums[-1])
        break