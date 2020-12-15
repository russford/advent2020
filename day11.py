directions = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if a or b]

def count_grid (grid, x, y, c):
    count = 0
    for i, j in directions:
        if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
            if grid[x + i][y + j] == c: count += 1
    return count

def iterate_grid_1(grid):
    g2 = [g.copy() for g in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and count_grid(grid, i, j, "#") == 0:
                g2[i][j] = "#"
            if grid[i][j] == "#" and count_grid(grid, i, j, "#") >= 4:
                g2[i][j] = "L"
    return [g for g in g2]


def count_grid_2 (grid, x, y, c):
    count = 0
    for i,j in directions:
        dist = 1
        while 0 <= x + dist*i < len(grid) and 0 <= y + j*dist < len(grid[0]) and grid[x+dist*i][y+dist*j] == ".":
            dist += 1
        if 0 <= x + dist*i < len(grid) and 0 <= y + j*dist < len(grid[0]) and grid[x+dist*i][y+dist*j] == c:
            count += 1
    return count

def iterate_grid_2(grid):
    g2 = [g.copy() for g in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and count_grid_2(grid, i, j, "#") == 0:
                g2[i][j] = "#"
            if grid[i][j] == "#" and count_grid_2(grid, i, j, "#") >= 5:
                g2[i][j] = "L"
    return [g for g in g2]

def part1 (grid):
    while True:
        # print ('\n'.join([''.join(g) for g in grid])+'\n')
        grid_2 = iterate_grid_1(grid)
        if all([grid[i] == grid_2[i] for i in range(len(grid))]):
            break
        grid = grid_2
    return sum([sum([1 if c == "#" else 0 for c in g])for g in grid])

def part2 (grid):
    while True:
        # print ('\n'.join([''.join(g) for g in grid])+'\n')
        grid_2 = iterate_grid_2(grid)
        if all([grid[i] == grid_2[i] for i in range(len(grid))]):
            break
        grid = grid_2
    return sum([sum([1 if c == "#" else 0 for c in g])for g in grid])


with open ("day11.txt", "r") as f:
    grid = [list(l) for l in f.read().splitlines()]

print (part1(grid))
print (part2(grid))


