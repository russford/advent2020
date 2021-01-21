card_key, door_key  = 6270530, 14540258

# card_key, door_key = 5764801, 17807724


def mod_exp (base, exp, modulo):
    prod = 1
    while exp:
        if exp & 1:
            prod = (prod * base) % modulo
        base = (base * base) % modulo
        exp >>= 1
    return prod

def solve_key(key, base, modulo):
    prod = 1
    for i in range(modulo):
        if key == prod:
            return i
        else:
            prod = (prod * base) % modulo

card_loop = solve_key(card_key, 7, 20201227)
door_loop = solve_key(door_key, 7, 20201227)

print (card_loop, door_loop)

print (mod_exp(card_key, door_loop, 20201227))
print (mod_exp(door_key, card_loop, 20201227))