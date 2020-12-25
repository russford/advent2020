
def set_value (mask, value):
    numstr = "{:036b}".format(value)
    return int(''.join([numstr[i] if mask[i] == "X" else mask[i] for i in range(36)]),2)

def part1 (program):
    mems = {}
    mask = ""
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            address = int(line[4:line.index("]")])
            value = int(line[line.index("=")+1:])
            mems[address] = set_value (mask, value)
    print (sum(mems.values()))

def store_values (mask, base_address, storage, value):
    pattern = [i for i,c in enumerate(mask[::-1]) if c == "X"]
    n = len(pattern)
    base_result = int(mask.replace("X", "0"), 2) | base_address
    base_result &= ~sum([1 << pattern[i] for i in range(n)])

    for num in range(2 ** n):
        var_bits = sum([1 << pattern[i] for i in range(n) if num >> i & 1])
        address = var_bits + base_result
        storage[address] = value

def part2 (program):
    mems = {}
    for line in program:
        if line.startswith ("mask"):
            mask = line[7:]
        else:
            address = int(line[4:line.index("]")])
            value = int(line[line.index("=")+1:])
            store_values(mask, address, mems, value)


    print (sum(mems.values()))

# 2753563653330



with open("day14.txt", "r") as f:
    program = f.read().splitlines()
part1 (program)

# program = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1""".splitlines()

part2 (program)

