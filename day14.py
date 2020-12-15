with open("day14.txt", "r") as f:
    program = f.read().splitlines()

mems = {}
mask = ""

def set_value (mask, value):
    numstr = "{:036b}".format(value)
    return int(''.join([numstr[i] if mask[i] == "X" else mask[i] for i in range(36)]),2)


for line in program:
    if line[:4] == "mask":
        mask = line[7:]
    else:
        address = int(line[4:line.index("]")])
        value = int(line[line.index("=")+1:])
        mems[address] = set_value (mask, value)
        print (sum([1 for c in mask if c == "X"]))

print (sum(mems.values()))




