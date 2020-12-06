def read_input(fname="input.txt"):
    with open(fname) as f:
        out = []
        for line in f.readlines():
            if line == "\n":
                yield out
                out = []
            else:
                out.append(set(line.strip()))
        yield out

def process_input(f, allforms):
    out = 0
    for forms in allforms:
        curset = set()
        curform = 0
        for form in forms:
            if curform == 0:
                curset = form
                curform += 1
            else:
                curset = f(curset, form)
        out += len(curset)
    return out

inp = list(read_input())
print("part1:\t", process_input(set.union, inp))
print("part2:\t", process_input(set.intersection, inp))
