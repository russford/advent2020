def check_height (d):
    if d[-2:] == "cm":
        return 150 <= int(d[:-2]) <= 193
    if d[-2:] == "in":
        return 59 <= int(d[:-2]) <= 76
    return False

def check_color (d):
    if d[0] == "#":
        a = int(d[1:], 16)
        if len(d) == 7: return True
    return False

validation = {
    "byr": lambda d: 1920 <= int(d) <= 2002,
    "iyr": lambda d: 2010 <= int(d) <= 2020,
    "eyr": lambda d: 2020 <= int(d) <= 2030,
    "hgt": check_height,
    "hcl": check_color,
    "ecl": lambda d: d in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda d: len(d) == 9 and d.isdigit(),
}


def is_complete(passport):
    return all([field in passport for field in validation.keys()])


def is_valid(passport):
    try:
        return all([func(passport[field]) for field, func in validation.items()])
    except:
        return False


def gen_passport (data):
    return {d[0]:d[1] for d in [l.split(":") for l in data.split()]}


data_str = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split ('\n\n')

with open ("day04.txt", "r") as f:
    data_str = f.read().split('\n\n')

passports =[gen_passport(l) for l in data_str]
print (len(list(passports)))
passports = list(filter(is_complete, passports))
print (len(passports))
passports = filter(is_valid, passports)
print (len(list(passports)))






