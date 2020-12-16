def read_input(fname="input.txt"):
    out = [{}, [], []]
    p = 0
    with open(fname) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                p += 1
                continue
            if p == 0:
                line = line.replace(" or ", ":").replace(" ", "").replace("-", ":")
                ls = line.split(":")
                out[0][ls[0]] = set()
                out[0][ls[0]] = out[0][ls[0]].union(set(range(int(ls[1]), int(ls[2])+1)))
                out[0][ls[0]] = out[0][ls[0]].union(set(range(int(ls[3]), int(ls[4])+1)))
            if p == 1:
                if line != "your ticket:":
                    out[1] = [int(i) for i in line.split(",")]
            if p == 2:
                if line != "nearby tickets:":
                    out[2].append([int(i) for i in line.split(",")])
    return out

## this wasted many time
## there were tickets that had 0 as the invalid value
## this broke the algorithm i had for part 2
def check_invalidity(fields, ticket):
    found_invalid = False
    s = 0
    for t in ticket:
        for k in fields:
            if t in fields[k]:
                break
        else:
            found_invalid = True
            s += t
    return (s, found_invalid) # <- the solution was to return a tuple

def get_scanning_rate(fields, tickets):
    s = 0
    for ticket in tickets:
        s += check_invalidity(fields, ticket)[0]
    return s

def find_field_indices(fields, tickets):
    out = {}
    tickets_ = [ticket[:] for ticket in tickets]
    for ticket in tickets:
        if check_invalidity(fields, ticket)[1]:
            tickets_.remove(ticket)
    num_fields = len(fields)
    ps = {}
    for field in fields:
        possible = list(range(num_fields))
        for ticket in tickets_:
            for i in range(num_fields):
                if i not in possible:
                    continue
                if ticket[i] not in fields[field]:
                    possible.remove(i)
        ps[field] = possible
    while ps:
        to_remove = []
        for field in ps:
            if not ps[field]:
                to_remove.append(field)
            if len(ps[field]) == 1:
                val = ps[field][0]
                out[field] = ps[field][0]
                for p in ps:
                    if val in ps[p]:
                        ps[p].remove(val)
                break
        for field in to_remove:
            del ps[field]
    return out

def mult_departures(fields, ticket):
    out = 1
    for f in fields:
        if "departure" in f:
            out *= ticket[fields[f]]
    return out

inp = read_input("input.txt")
print("part1:\t", get_scanning_rate(inp[0], inp[2]))
indices = find_field_indices(inp[0], inp[2])
print("part2:\t", mult_departures(indices, inp[1]))
