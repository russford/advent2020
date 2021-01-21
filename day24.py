import re
from collections import defaultdict

steps = {"e":  (1, -1),
         "se": (0, -1),
         "sw": (-1, 0),
         "w":  (-1, 1),
         "nw": (0,  1),
         "ne": (1,  0)}

def hex_neighbors (x, y):
    return [(x+dx, y+dy) for dx, dy in steps.values()]

def neighbor_count (x, y, hash):
    return sum([hash[i,j] for i,j in hex_neighbors(x,y)])


with open("day24.txt", "r") as f:
    dirs = [re.findall("(e|se|sw|w|nw|ne)", l) for l in f.read().splitlines()]

# part 1
hash_map = defaultdict(int)
for dir in dirs:
    end_coord = tuple([sum(a) for a in zip(*[steps[b] for b in dir])])
    hash_map[end_coord] = 0 if hash_map[end_coord] else 1

print (sum(hash_map.values()))

# part 2
for day in range(100):
    new_hash = defaultdict(int)
    for x, y in hash_map.keys():
        if hash_map[x,y]:
            for dx, dy in steps.values():
                new_hash[x+dx, y+dy] = 0
            new_hash[x,y] = 0

    for x, y in new_hash.keys():
        neighbors = neighbor_count(x,y,hash_map)
        if neighbors == 2 or (neighbors == 1 and hash_map[x,y]):
            new_hash[x,y] = 1
        # if hash_map[x, y] == 1 and neighbors == 1 or neighbors == 2:
        #     new_hash[x, y] = 1
        # if hash_map[x, y] == 0 and neighbors == 2:
        #     new_hash[x, y] = 1
    hash_map = new_hash
print (sum(hash_map.values()))






