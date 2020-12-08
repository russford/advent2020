import string

def part1(data):
    print(sum([len(set(s.replace("\n", ""))) for s in data]))


def part2(data):
    print(sum(
        [sum(
            [1 if all([c in l for l in d.split()]) else 0
                for c in string.ascii_lowercase]
            )
            for d in data]
    ))



test_data = """abc

a
b
c

ab
ac

a
a
a
a

b""".split ('\n\n')

with open ("day06.txt", "r") as f:
    data = f.read().split('\n\n')


part1(data)
part2(data)



