import numpy as np
with open('8_in.txt', 'r') as f:
    line = f.readline()

elems = np.array(line.split(' ')).astype(np.int)

metadatas = []

def parse_child(t_elems, idx_st, metadatas):
    curr_idx = idx_st
    n_childs = t_elems[curr_idx]
    n_metadata = t_elems[curr_idx + 1]
    curr_idx += 2
    for _ in range(n_childs):
        curr_idx, metadatas = parse_child(t_elems, curr_idx, metadatas)
    metadatas += t_elems[curr_idx:curr_idx + n_metadata].tolist()
    return curr_idx + n_metadata, metadatas

idx, met = parse_child(elems, 0, [])
print(np.sum(met))

def get_node_value(t_elems, idx_st):
    curr_idx = idx_st
    n_childs = t_elems[curr_idx]
    n_metadata = t_elems[curr_idx + 1]
    curr_idx += 2
    if n_childs == 0:
        value = np.sum(t_elems[curr_idx:curr_idx + n_metadata])
    else:
        child_values = np.zeros(n_childs, dtype=np.int)
        for i in range(n_childs):
            curr_idx, t_value = get_node_value(t_elems, curr_idx)
            child_values[i] = t_value
        value = 0
        for t_m in t_elems[curr_idx:curr_idx + n_metadata]:
            if t_m > 0 and t_m <= n_childs:
                value += child_values[t_m-1]
    
    return curr_idx + n_metadata, value

idx, val = get_node_value(elems, 0)
print(val)