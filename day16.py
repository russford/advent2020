import re

def part1 (rules, my_ticket, tickets):
    numbers = list(map(int, re.findall("\d+", rules)))
    brackets = list(zip(numbers[::2], numbers[1::2]))
    invalids = []
    for v in map(int, re.findall("\d+", tickets)):
        if not any ([low <= v <= high for low, high in brackets]):
            invalids.append(v)
    print (sum(invalids))


def is_valid (ticket, brackets):
    return all([any([l <= v <= h for l, h in brackets]) for v in ticket])


def get_valid_tickets (rules, my_ticket, tickets):
    all_tickets = [list(map(int, l.split(','))) for l in my_ticket.split('\n')[1:] + tickets.split('\n')[1:]]
    numbers = list(map(int, re.findall("\d+", rules)))
    brackets = list(zip(numbers[::2], numbers[1::2]))
    # return [list(t) for t in filter(lambda t: is_valid(t, brackets), all_tickets)]
    return list(filter(lambda t: is_valid(t, brackets), all_tickets))


def build_rules (rules_list):
    return {g[0]:list(map(int,g[1:])) for g in re.findall("(.+): (\d+)-(\d+) or (\d+)-(\d+)", rules_list) }


def check_range(v, rule):
    try:
        return rule[0] <= v <= rule[1] or rule[2] <= v <= rule[3]
    except Exception as e:
        print (v, rule)
        raise e


def part2 (rules_list, my_ticket, tickets):
    rules = build_rules(rules_list)
    tickets = get_valid_tickets(rules_list, my_ticket, tickets)
    matchup = {}
    for field in rules.keys():
        matchup[field] = []
        for i in range(len(rules)):
            if all([check_range(t[i], rules[field]) for t in tickets]):
                matchup[field].append(i)
    matches = {}
    while len(matches) < len(rules):
        for field, poss in matchup.items():
            if len(poss) == 1:
                match = poss[0]
                matches[field] = match
                for list in matchup.values():
                    if match in list: list.remove(match)

    product = 1
    for field, column in matches.items():
        if field.startswith("departure"):
            print (field, tickets[0][column])
            product *= tickets[0][column]
    print (product)


with open ("day16.txt", "r") as f:
    rules_list, my_ticket, tickets = f.read().split('\n\n')

part1(rules_list, my_ticket, tickets)
part2(rules_list, my_ticket, tickets)


