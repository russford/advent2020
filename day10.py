def part1 (bag):
    ones, threes = 0,0
    for i in range(1, len(bag)):
        if bag[i]-bag[i-1] == 3:
            threes += 1
        elif bag[i]-bag[i-1] == 1:
            ones += 1
        else:
            print(i, bag[i], bag[i-1])
            raise Exception
    print(ones* threes)

def part2 (bag):
    queue = [[0]]
    found = 0
    while queue:
        plug = queue.pop()
        if plug[-1] == data[-1]:
            found += 1
            print (plug)
        else:
            b = bag.index(plug[-1])
            next_three = bag[b+1:b+4]
            adapters = [a for a in next_three if 0 < a-plug[-1] <= 3]
            if adapters:
                queue += [plug+[a] for a in adapters]
    print (found)


def part2(data):
    chains = []
    group = 1
    i = 1
    while i < len(data):
        if data[i] == data[i-1]+1:
            group += 1
        else:
            chains.append(group)
            group = 1
        i += 1
    print(data)
    print(chains)
    counters = {1:1, 2:1, 3:2, 4:4, 5:7, 6:13, 7:24}

    count = 1
    for c in chains:
        count *= counters[c]

    print (count)


with open("day10.txt", "r") as f:
    data = [0] + sorted([int(a) for a in f.read().splitlines()])
data += [data[-1]+3]

part1(data)
part2(data)

