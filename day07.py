import re


def build_rule_set (rule_str, part):
    d = {}
    for rule in rule_str:
        outer_bag = rule[:rule.index("bags")-1]
        d[outer_bag] = []
        inner_bags = re.findall("\d+ \w+ \w+", rule)
        for bag_rule in inner_bags:
            i = bag_rule.index(" ")
            #
            if part == 1:
                d[outer_bag].append(bag_rule[i+1:])
            else:
                d[outer_bag].append((int(bag_rule[:i]), bag_rule[i + 1:]))
    return d


def part1 (rules, bagtype):
    outer_bags = [k for k,v in rules.items() if bagtype in v]
    for bag in outer_bags:
        outer_bags += [k for k,v in rules.items() if bag in v and k not in outer_bags]
    return (outer_bags)


def bag_count (rules, bagtype):
    total = 0
    if rules[bagtype]:
        for b in rules[bagtype]:
            a = b[0] * bag_count (rules, b[1])
            print (b,a)
            total += a
        print(bagtype, total)
        return total + 1
    else:
        return 1


with open("day07.txt", "r") as f:
    data = f.read().splitlines()

test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()

rules = build_rule_set(data, 1)
bags = part1(rules, "shiny gold")
print(len(bags))

rules = build_rule_set (data, 2)
bags = bag_count(rules, "shiny gold") - 1
print(bags)






