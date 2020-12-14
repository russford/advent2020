import re

with open("day13.txt", "r") as f:
    data = f.read()

def part1(data):
    data = [int(a) for a in re.findall("\d+", data)]
    timestamp = data[0]
    buses = data[1:]
    times = [((timestamp//b+1)*b-timestamp, b) for b in buses]
    bus = sorted(times, key=lambda a:a[0])[0]
    print (bus[0]*bus[1])


def solve_mult_mod (modulos):
    modulos.sort(key=lambda a:-a[0])
    m = modulos[0][0]
    a = m - modulos[0][1]
    for i in range(1, len(modulos)):
        for j in range(modulos[i][0]):
            if (a + m*j + modulos[i][1]) % modulos[i][0] == 0:
                a += m*j
                m *= modulos[i][0]
                break
    return a

def part2(data):
    data = data.split('\n')[1]
    data = sorted([(int(a), i) for i, a in enumerate(data.split(',')) if a != "x" ], key=lambda a:-a[0])
    print(solve_mult_mod(data))

part1(data)
part2(data)

