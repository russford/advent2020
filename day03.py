from operator import mul
from functools import reduce


def part_i (trees, w):
    return sum([1 if l[(i*w[0])%len(l)] == "#" else 0 for i,l in enumerate(trees[::w[1]])])


def part2 (trees, walk):
    return reduce (mul, [part_i(trees, w) for w in walk], 1)


with open ("day03.txt", "r") as f:
    trees = [l.strip('\n') for l in f.readlines()]

print (part_i(trees, (3,1)))

walks = [(1,1), (3,1), (5,1), (7,1), (1,2)]

print (part2(trees, walks))
