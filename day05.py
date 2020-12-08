def bsp(str):
    return int(''.join(['1' if c in ["B", "R"] else '0' for c in str]), 2)


with open("day05.txt", "r") as f:
    ids = [bsp(d) for d in f.read().split('\n')]

print (max(ids))
for d in range(1, max(ids)):
    if d-1 in ids and d+1 in ids and not d in ids:
        print(d)


