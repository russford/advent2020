def move (pos, dir, dist):
    return [pos[i] + dirs[dir][i] * dist for i in range(2)]

def move_to_wp (pos, wp, n):
    return [pos[i] + wp[i]*n for i in range(2)]

def rotate90(vec, neg):
    c = complex(vec[0],vec[1])
    c = c*complex(0, -1 if neg else 1)
    return int(c.real), int(c.imag)

with open("day12.txt", "r") as f:
    data = [(l[0], int(l[1:])) for l in f.read().splitlines()]

dirs = { "E":(1,0), "N":(0,1), "W":(-1,0), "S":(0,-1) }
dir_keys = list(dirs.keys())
pos = [0,0]
dir = "E"

for d in data:
    if d[0] in ["E", "S", "N", "W"]:
        pos = move(pos, d[0], d[1])
    elif d[0] in ["R", "L"]:
        d_index = dir_keys.index(dir)
        dir = dir_keys[(d_index + (d[1]//90)*(-1 if d[0] == 'R' else 1)) % 4]
    elif d[0] == "F":
        pos = move(pos, dir, d[1])
    else:
        print ("bad instruction {}".format(d))

print (abs(pos[0])+abs(pos[1]))

pos = [0,0]
dir = "E"
wp = (10,1)

for d in data:
    if d[0] in ["E", "S", "N", "W"]:
        wp = move(wp, d[0], d[1])
    elif d[0] in ["R", "L"]:
        for i in range(d[1] // 90):
            wp = rotate90(wp, d[0] == 'R')
    elif d[0] == "F":
        pos = move_to_wp(pos, wp, d[1])
    else:
        print ("bad instruction {}".format(d))
    print (d, pos, wp, dir)

print (abs(pos[0])+abs(pos[1]))
