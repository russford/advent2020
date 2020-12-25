from collections import Counter

def rotate_grid(grid):
    n = len(grid)
    return [[grid[n - y - 1][x] for y in range(n)] for x in range(n)]

def flip_grid(grid):
    n = len(grid)
    return [list(g[::-1]) for g in grid]

class Tile (object):
    def __init__ (self, init_str):
        data = init_str.split('\n')
        self.id = int(data[0][5:9])
        self.grid = [list(l) for l in data[1:]]
        self.edges = []
        self.generate_edges()
        self.orientation = -1

    def __str__(self):
        return "\n".join([''.join(g) for g in self.grid])

    def rotate90 (self):
        self.grid = rotate_grid(self.grid)

    def flip(self):
        self.grid = flip_grid(self.grid)

    def generate_edges(self):
        self.edges = []
        f_str = "{:0" + str(len(self.grid)) + "b}"
        for e in range(4):
            edge = self.get_edge(e)
            self.edges += [edge, int(f_str.format(edge)[::-1], 2)]

    def get_edge (self, edge):
        n = len(self.grid)
        generate = [(0,0,0,1), (0, n-1, 1, 0), (n-1, 0, 0, 1), (0, 0, 1, 0)]
        sx, sy, dx, dy = generate[edge]
        return sum([1 << (n-i-1) if self.grid[sx+dx*i][sy+dy*i] == "#" else 0 for i in range(n)])

    def match_edge (self, target, edge_no):
        gen_edges= []
        for i in range(8):
            e = self.get_edge(edge_no)
            gen_edges.append(e)
            if e == target: break
            self.rotate90()
            if i == 3: self.flip()
        else:
            raise Exception ("couldn't match edge {}".format(target))

    def orient_in_corner(self, edge_counts):
        for i in range(4):
            e = self.get_edge(0)
            if edge_counts[e] == 1: break
            self.rotate90()
        else:
            raise Exception("no edge counts for {} were 1")
        if edge_counts[self.get_edge(1)] == 1:
            self.flip()
        checker = [(0, 1), (1, 2), (2, 2), (3, 1)]
        for c, n in checker:
            if edge_counts[self.get_edge(c)] != n:
                raise Exception ("failed edge check")

    def get_line (self, m):
        return ''.join(self.grid[m][1:-1])


def find_and_align (edge, edge_no, placed, tiles):
    target_tiles = [t for t in tiles if target_edge in t.edges and t not in placed.values()]
    if len(target_tiles) != 1:
        raise Exception("target tile list: {}".format(target_tiles))
    target_tiles[0].match_edge(target_edge, edge_no)
    return target_tiles[0]


def check_alignment (n_grid, placed):
    m = len(placed[0,0].grid)
    for x in range(n_grid - 1):
        for y in range(n_grid * m):
            if placed[x,y // m].grid[y % m][m-1] != placed[x+1, y//m].grid[y % m][0]:
                raise Exception ("mismatch on vertical line {} {}".format (x, y))
    for y in range(n_grid - 1):
        for x in range(n_grid * m):
            if placed[x // m, y].grid[m-1][x % m] != placed[x // m, y+1].grid[0][x % m]:
                raise Exception ("mismatch on horizontal line {} {}".format (x, y))


def build_master_grid (n_grid, placed):
    m = len(placed[0,0].grid)-2
    g2 = []
    for y in range(n_grid * m):
        row = []
        for x in range(n_grid):
            row.append(placed[x, y//m].grid[(y % m)+1][1:-1])
        row = [r for l in row for r in l]
        g2.append(row)
    return g2

def scan_pattern(grid, pattern):
    pat_x = max([a[0] for a in pattern])
    pat_y = max([a[1] for a in pattern])
    finds = 0
    for i in range(len(grid) - pat_x):
        for j in range(len(grid) - pat_y):
            if all ([grid[j+py][i+px] == "#" for px, py in pattern]):
                print("found at ", i, j)
                finds += 1
                for px, py in pattern:
                    grid[py + j][px + i] = 'O'
    if finds:
        print("\n".join([''.join(g) for g in grid]))
        print(sum([1 for g in grid for c in g if c == "#"]))
        return 1
    else:
        return 0

def remove_monsters(grid):
    monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')
    pattern = [(x,y) for x in range(len(monster[0])) for y in range(len(monster)) if monster[y][x] == "#"]
    print (pattern)
    for i in range(8):
        if scan_pattern(grid, pattern):
            break
        grid = rotate_grid(grid)
        if i == 3: grid = flip_grid(grid)
    else:
        print ("couldn't find any monsters")


with open("day20.txt", "r") as f:
    tile_list = f.read().split("\n\n")

tiles = [Tile(tile_str) for tile_str in tile_list]
edge_list = [e for t in tiles for e in t.edges]
edge_counts = Counter(edge_list)

# part 1
corners = [t for t in tiles if sum([edge_counts[e] for e in t.edges]) == 12]
product = 1
for c in corners:
    product *= c.id
print (product)

# part 2
n_grid = int(len(tiles) ** 0.5)
placed = { (0,0): corners[0] }
corners[0].orient_in_corner(edge_counts)

for x in range(n_grid):
    if x > 0:
        target_edge = placed[x-1,0].get_edge(1)
        placed[x, 0] = find_and_align(target_edge, 3, placed, tiles)
    for y in range(1, n_grid):
        target_edge = placed[x,y-1].get_edge(2)
        placed[x, y] = find_and_align(target_edge, 0, placed, tiles)

for y in range(n_grid):
    print (" ".join([str(placed[x,y].id) for x in range(n_grid)]))

check_alignment(n_grid, placed)
master = build_master_grid(n_grid, placed)
remove_monsters(master)



















