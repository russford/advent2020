test_input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

with open("day21.txt", "r") as f:
    input = f.read().splitlines()

problem = []
for line in input:
    ingredients = line[:line.index("(")-1].split(" ")
    allergens = line[line.index("contains")+9:-1].split(", ")
    problem.append((ingredients, allergens))

ingredient_set = set([item for recipe in problem for item in recipe[0]])
allergen_set = set([item for recipe in problem for item in recipe[1]])

poss = {}
for allergen in allergen_set:
    l = [p[0] for p in problem if allergen in p[1]]
    poss[allergen] = set(l[0]).intersection(*l)

found = {}
while len(found) < len(poss):
    for allergen, l in poss.items():
        if len(l) == 1:
            for e in l: break
            found[allergen] = e
            for list in poss.values():
                if e in list: list.remove(e)
print (sum([1 for recipe in problem for item in recipe[0] if item not in found.values()]))

print(",".join(v for k, v in sorted(found.items(), key=lambda a:a[0])))


