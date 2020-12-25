def neighbors_3d (x, y, z):
    return [(x+a, y+b, z+c)
        for a in range(-1, 2)
        for b in range(-1, 2)
        for c in range (-1, 2) if a or b or c]

def build_space_3d (input):
    return { (x,y,0): 1 for x in range(len(input)) for y in range(len(input[0])) if input[x][y] == "#" }

def neighbors_4d (x, y, z, w):
    return [(x+a, y+b, z+c, w+d)
        for a in range(-1, 2)
        for b in range(-1, 2)
        for c in range (-1, 2)
        for d in range (-1, 2) if a or b or c or d]

def build_space_4d (input):
    return { (x,y,0,0): 1 for x in range(len(input)) for y in range(len(input[0])) if input[x][y] == "#" }

def count_active(space, point, n_func):
    return sum([1 for n in n_func(*point) if n in space and space[n]])


def iterate_space (space, n_func):
    new_space = {}
    for point in space:
        new_space[point] = 0
        for n in n_func(*point):
            new_space[n] = 0
    for point in new_space:
        active = count_active(space, point, n_func)
        is_active = point in space and space[point]
        if is_active and active in [2,3]:
            new_space[point] = 1
        if not is_active and active == 3:
            new_space[point] = 1
    inactive_list = [k for k,v in new_space.items() if not v]
    for point in inactive_list:
        del new_space[point]
    return new_space


input = """..#..#..
.###..#.
#..##.#.
#.#.#.#.
.#..###.
.....#..
#...####
##....#.""".splitlines()

test_input = """.#.
..#
###""".splitlines()

space = build_space_3d(input)
for i in range(6):
    space = iterate_space(space, neighbors_3d)
    print (len(space))

space = build_space_4d(input)
for i in range(6):
    space = iterate_space(space, neighbors_4d)
    print (len(space))



