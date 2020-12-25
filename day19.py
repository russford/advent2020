import re

with open("day19.txt", "r") as f:
    rules_list, messages = f.read().split('\n\n')

made_rules = { g[0]:g[1] for g in re.findall('(\d+): \"(\w+)\"', rules_list) }

def get_rule_length (r):
    if rules[r] in ["a", "b"]:
        return 1
    else:
        return sum([get_rule_length(a) for a in rules[r][0].split(" ")])

def check_match (str, match, position, rules):
    print ("finding a match for {} at position {}".format(rules[match], position))
    if position >= len(str): return False, 0
    if rules[match] in ["a", "b"]:
        return str[position] == rules[match], 1
    else:
        for poss in rules[match]:
            pattern_length = 0
            for item in poss.split(' '):
                result, delta = check_match(str, item, position+pattern_length, rules)
                if not result: break
                pattern_length += delta
            else:
                print ("found match for {}: returning length {}".format(rules[match], pattern_length))
                return True, pattern_length
        # print ("no match")
        return False, 0

def build_match_lists (rules, item, n):
    matches = []
    for i in range(2**n):
        pattern = ("{:0"+str(n)+"b}").format(i).replace("0", "a").replace("1", "b")
        result, length = check_match(pattern, item, 0, rules)
        if result:
            matches.append(pattern)
    return matches

rules = {}
for rule in rules_list.split('\n'):
    if "\"" in rule:
        rules[rule[:rule.index(":")]] = rule[rule.index("\"")+1]
    else:
        rules[rule[:rule.index(":")]] = rule[rule.index(":")+2:].split(" | ")

rule_lengths = { r:get_rule_length(r) for r in rules.keys() }
for k, v in sorted(rule_lengths.items(), key=lambda v: -v[1]):
    print (k, v)

n = rule_lengths["31"]
matches = { i:build_match_lists(rules, i, n) for i in ["31", "42"]}

new_list = []
for m in messages.split('\n'):
    pattern = ""
    if len(m) % n == 0:
        for i in range(len(m) // n):
            if m[i*n:i*n+n] in matches["42"]:
                pattern += "A"
            elif m[i*n:i*n+n] in matches["31"]:
                pattern += "B"
            else:
                break
        else:
            new_list.append(pattern)

print (len(messages.split('\n')))
# print ("\n".join(new_list))
found = 0
for msg in new_list:
    if "A" in msg and "B" in msg:
        b_count = 0
        while msg[-1-b_count] == "B":
            b_count += 1
        if len(msg) > 2*b_count:
            if msg[-2*b_count:] == "A"*b_count + "B"*b_count and msg[:-2*b_count] == "A"*(len(msg)-2*b_count):
                found += 1
print (found)









