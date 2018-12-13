import numpy as np
from collections import Counter
coords = []

with open('6_in.txt', 'r') as f:
    for line in f:
        t_elem = line.split(',')
        coords.append([int(t_elem[0]), int(t_elem[1])])

coords = np.array(coords)
max_x = np.max(coords[:, 0])
max_y = np.max(coords[:, 1])

grid = np.zeros((max_x, max_y), dtype=np.int)

for t_x in range(max_x):
    for t_y in range(max_y):
        t_coord = np.array([t_x, t_y])
        closest = np.argmin(np.sum(np.abs(coords - t_coord), axis=-1)) + 1
        grid[t_x, t_y] = closest

borders = [grid[0, :], grid[:, 0], grid[-1, :], grid[:, -1]]
infinite = np.unique(np.concatenate(borders))

for t_elem in infinite:
    grid[grid == t_elem] = -1

counts = {}
for t_elem in np.unique(grid):
    if t_elem == -1:
        continue
    counts[t_elem] = np.sum(grid == t_elem)
print(max(counts.values()))


max_distance = 10000
region_size = 0

for t_x in range(0, max_x):
    for t_y in range(0, max_y):
        t_coord = np.array([t_x, t_y])
        t_d = np.sum(np.sum(np.abs(coords - t_coord), axis=-1))
        if t_d < max_distance:
            region_size += 1

print(region_size)