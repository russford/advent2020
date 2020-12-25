import re
from collections import defaultdict

steps = {"e":  (1, -1),
         "se": (0, -1),
         "sw": (-1, 0),
         "w":  (-1, 1),
         "nw": (0,  1),
         "ne": (1,  0)}

def count_neighbors (hashmap, x, y):
    return



with open("day24test.txt", "r") as f:
    dirs = [re.findall("(e|se|sw|w|nw|ne)", l) for l in f.read().splitlines()]


# part 1
hash_map = defaultdict(int)
for dir in dirs:
    end_coord = tuple([sum(a) for a in zip(*[steps[b] for b in dir])])
    if end_coord in hash_map:
        del hash_map[end_coord]
    else:
        hash_map[end_coord] = 1

print (sum(hash_map.values()))

for day in range(100):
    new_hash = defaultdict(int)
    for x, y in hash_map.keys():
        for dx, dy in steps.values():
            new_hash[x+dx, y+dy] = 0
    for x, y in new_hash.keys():
        neighbors = sum([1 for dx, dy in steps.values() if hash_map[x+dx,y+dy] == 1])
        if hash_map[x,y] == 1 and neighbors == 0 or neighbors > 2:
            new_hash[x,y] = 0
        if hash_map[x,y] == 0 and neighbors == 2:
            new_hash[x,y] = 1
    hash_map = defaultdict(int)
    for k, v in new_hash.items():
        if v: hash_map[k] = 1
    print (day, sum(hash_map.values()))






