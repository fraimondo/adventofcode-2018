import numpy as np


class Node():
    def __init__(self, value):
        self._next = self
        self._prev = self
        self._value = value

class CircularList():
    def __init__(self):
        self._current = None
    
    def insert(self, value):
        new = Node(value)
        if self._current is None:
            self._current = new
        else:
            new._prev = self._current
            new._next = self._current._next
            self._current._next._prev = new
            self._current._next = new
            self._current = new
    
    def cur_value(self):
        return self._current._value

    def delete(self):
        t_prev = self._current._prev
        t_next = self._current._next
        t_prev._next = t_next
        t_next._prev = t_prev
        self._current = t_next
    
    def clockwise(self, n):
        for _ in range(n):
            self._current = self._current._next
    
    def counter_clockwise(self, n):
        for _ in range(n):
            self._current = self._current._prev


n_marbles = 71498 * 100
n_players = 465
scores = {k: [] for k in range(n_players)}

marbles = CircularList()
marbles.insert(0)

first = marbles._current

cur_idx = 0
cur_player = 0

for this_marble in range(1, n_marbles):
    if this_marble % 23 != 0:
        marbles.clockwise(1)
        marbles.insert(this_marble)
    else:
        scores[cur_player].append(this_marble)
        marbles.counter_clockwise(7)
        scores[cur_player].append(marbles.cur_value())
        marbles.delete()
    cur_player = (cur_player + 1) % n_players
total_scores = [np.sum(v) for v in scores.values()]
print(np.max(total_scores))