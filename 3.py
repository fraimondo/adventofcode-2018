import numpy as np

def parse_claim(line):
    a = line.split('@')[1]
    pos, size = a.split(':')
    pos_x, pos_y = pos.split(',')
    w, h = size.split('x')
    return int(pos_x), int(pos_y), int(w), int(h)

claims = []
with open('3_in.txt', 'r') as f:
    for line in f:
        claims.append(parse_claim(line))

claims = np.array(claims)

max_width = np.max(claims[:, 0] + claims[:, 2])
max_height = np.max(claims[:, 1] + claims[:, 3])

uses = np.zeros((max_width, max_height))

for t_x, t_y, w, h in claims:
    uses[t_x:t_x+w, t_y:t_y+h] += 1

print(np.sum(uses > 1))