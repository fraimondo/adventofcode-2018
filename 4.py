import pandas as pd
import datetime as dt
import re
import numpy as np

events = {'ts': [], 'desc': []}

with open('4_in.txt', 'r') as f:
    for line in f:
        ts = line[:18]
        events['ts'].append(ts)
        events['desc'].append(line[18:])
        #find number of guard

df = pd.DataFrame(events)
df = df.sort_values(by='ts')
guards = []
types = []
desc = df['desc'].values
match = re.search(r"#[0-9]+", desc[0])
t_guard = int(match.group(0)[1:])
guards.append(t_guard)
types.append('begin')

for i, value in enumerate(desc[1:]):
    match = re.search(r"#[0-9]+", value)
    if match is not None:
        t_guard = int(match.group(0)[1:])
    guards.append(t_guard)
    if 'begins' in value:
        types.append('begin')
    elif 'wakes' in value:
        types.append('wake')
    elif 'asleep' in value:
        types.append('sleep')

df['Guard'] = guards
df['Type'] = types
df = df.sort_values(by='ts')

df = df[df['Type'].isin(['sleep', 'wake'])]
df['min'] = [x[15:17] for x in df['ts'].values]

values = df[['Guard', 'min', 'Type']].values.reshape(-1, 6)


idx_guards = np.unique(df['Guard']).tolist()
data_guards = np.zeros((len(idx_guards), 60))
for row in values:
    t_idx = idx_guards.index(row[0])
    st = int(row[1])
    end = int(row[4])
    data_guards[t_idx, st:end] += 1

max_slept = np.max(np.sum(data_guards, axis=1))
idx_max = np.argmax(np.sum(data_guards, axis=1))

best_minute = np.argmax(data_guards[idx_max])
print(idx_guards[idx_max] * best_minute)

idx = np.unravel_index(np.argmax(data_guards), data_guards.shape)
print(idx_guards[idx[0]] * idx[1])