import re
import numpy as np

needed = {}
with open('7_in.txt', 'r') as f:
    for line in f:
        pre = re.search(r"Step [A-Z]", line).group(0)[-1]
        post = re.search(r"[A-Z] can", line).group(0)[0]
        if post not in needed:
            needed[post] = []
        needed[post].append(pre)

elems = [elem for l in needed.values() for elem in l]
elems += needed.keys()
elems = set(elems)

for t_e in elems:
    if t_e not in needed:
        needed[t_e] = []

# find the root
root = sorted([k for k, v in needed.items() if len(v) == 0])[0]
order = [root]

while len(order) < len(elems):
    t_needed = {k: [t_v for t_v in v if t_v not in order] for k, v in needed.items() if k not in order}
    t_elem = sorted([x for x, v in t_needed.items() if len(v) == 0])[0]
    order.append(t_elem)

print(''.join(order))

durations = {k: 61 + i for i, k in enumerate(sorted(list(elems)))}

n_workers = 5
done = []
to_do = sorted([k for k, v in needed.items() if len(v) == 0])
tasks = {i: None for i in range(n_workers)}
timers = np.zeros(n_workers, dtype=np.int)
for i, t_i in enumerate(to_do[:5]):
    timers[i] = durations[t_i]
    tasks[i] = t_i
t = 0
while len(done) < len(elems):
    t += 1
    finishing = np.where(timers == 1)[0]
    for t_f in finishing:
        done.append(tasks[t_f])
        tasks[t_f] = None
    timers[timers != 0] -= 1
    t_needed = {k: [t_v for t_v in v if t_v not in done] 
                for k, v in needed.items() if k not in done}
    to_do = sorted([x for x, v in t_needed.items() if len(v) == 0 and x not in
                    tasks.values()])
    free = np.where(timers == 0)[0]
    n_to_do = len(to_do)
    for i in range(min(n_to_do, len(free))):
        timers[free[i]] = durations[to_do[i]]
        tasks[free[i]] = to_do[i] 

print(t)   




