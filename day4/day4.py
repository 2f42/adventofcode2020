def read_passport(pass_string):
    return { s.split(":")[0] : s.split(":")[1] for s in pass_string.split() }

def read_input(filename="input.txt"):
    out = []
    with open(filename) as f:
        cur = ""
        for line in f.readlines():
            if line == "\n":
                out.append(read_passport(cur))
                cur = ""
            else:
                cur += " " + line.strip()
        else:
            out.append(read_passport(cur))
    return out

def has_fields(required, passport):
    return required.issubset(passport.keys())

def validate(passport):
    o = has_fields({"byr", "eyr", "iyr", "hgt", "hcl", "ecl", "pid"}, passport)
    if o:
        byr = 2002 >= int(passport["byr"]) >= 1920
        iyr = 2020 >= int(passport["iyr"]) >= 2010
        eyr = 2030 >= int(passport["eyr"]) >= 2020
        hgt_t = passport["hgt"][-2:]
        hgt_v = 0
        if hgt_t in ["cm", "in"]: hgt_v = int(passport["hgt"][:-2])
        else: pass
        hgt = (hgt_t == "cm" and 193 >= hgt_v >= 150) or \
              (hgt_t == "in" and 76 >= hgt_v >= 59)
        hcl_h = passport["hcl"][0] == "#" and len(passport["hcl"]) == 7
        hcl_v = (False not in [c in "0123456789abcdef" \
                               for c in passport["hcl"][1:]])
        hcl = hcl_h and hcl_v
        ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", \
                                  "grn", "hzl", "oth"]
        pid = len(passport["pid"]) == 9
        pid &= (False not in [c in "0123456789" for c in passport["pid"]])
        o = byr and iyr and eyr and hgt and hcl and ecl and pid
    return o

def part1(inp):
    c = 0
    for p in inp:
        c += int(has_fields({"byr", "eyr", "iyr", "hgt", "hcl", "ecl", "pid"}, \
                            p))
    return c

def part2(inp):
    c = 0
    for p in inp:
        c += int(validate(p))
    return c

print(part2(read_input()))
