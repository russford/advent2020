import re


def is_valid_pwd_1 (g):
    rep = g[3].count(g[2])
    return int(g[0]) <= rep <= int(g[1])


def is_valid_pwd_2 (g):
    return (1 if g[3][int(g[0])-1] == g[2] else 0) + (1 if g[3][int(g[1])-1] == g[2] else 0) == 1


if __name__ == "__main__":
    with open("day02.txt", "r") as f:
        pwds = f.readlines()
    m = re.compile('(\d+)-(\d+) (\w): (\w+)')
    print(sum([1 if is_valid_pwd_1(m.match(p).groups()) else 0 for p in pwds]))
    print(sum([1 if is_valid_pwd_2(m.match(p).groups()) else 0 for p in pwds]))



