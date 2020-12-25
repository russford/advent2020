import re

def do_calc (calc_list):
    result = calc_list[0]
    calc_list = calc_list[1:]
    while calc_list:
        if calc_list[0] == "*":
            result = result * calc_list[1]
        else:
            result = result + calc_list[1]
        calc_list = calc_list[2:]
    return result


def do_calc_2 (calc_list):
    while "+" in calc_list:
        op_index = calc_list.index("+")
        calc_list = calc_list[:op_index-1] + [calc_list[op_index-1] + calc_list[op_index+1]] + calc_list[op_index+2:]
    while "*" in calc_list:
        op_index = calc_list.index("*")
        calc_list = calc_list[:op_index-1] + [calc_list[op_index-1] * calc_list[op_index+1]] + calc_list[op_index+2:]
    return calc_list[0]


def parse_calc(calc, func):
    input = [a if a in "()*+" else int(a) for a in re.findall("\d+|[*+()]", calc)]
    while ")" in input:
        end_index = input.index(")")
        start_index = end_index - input[:end_index][::-1].index("(")
        result = func(input[start_index:end_index])
        input = input[:start_index-1] + [result] + input[end_index+1:]
    return func (input)


with open("day18.txt", "r") as f:
    calcs = f.read().splitlines()

print (sum([parse_calc(c, do_calc) for c in calcs]))
print (sum([parse_calc(c, do_calc_2) for c in calcs]))
