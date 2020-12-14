def execute_code (program):
    acc = 0
    ip = 0
    while ip < len(program) and program[ip]:
        instr, value = program[ip].split(" ")
        if instr == "acc":
            acc += int(value)
        if instr == "jmp":
            next_ip = ip + int(value)
        else:
            next_ip = ip + 1
        program[ip] = ""
        ip = next_ip
        if ip == len(program):
            return 1, acc
    return 0, acc

program = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split('\n')

with open("day08.txt", "r") as f:
    program = f.read().splitlines()

result = execute_code(program.copy())
if result[0] == 0:
    print (result[1])

for i in range(len(program)):
    instr, value = program[i].split(" ")
    if instr in ["nop", "jmp"]:
        p = program.copy()
        p[i] = "{} {}".format("jmp" if instr == "nop" else "nop", value)
        result = execute_code(p)
        if result[0] == 1:
            print (result[1])
            break






