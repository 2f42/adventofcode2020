def part1():
    inp = []
    with open("input.txt") as f:
        inp = [int(line) for line in f.readlines()]
    for i in inp:
        for j in inp:
            if i+j == 2020:
                return i*j

def part2():
    inp = []
    with open("input.txt") as f:
        inp = [int(line) for line in f.readlines()]
    for i in inp:
        for j in inp:
            if i+j >= 2020:
                continue
            for k in inp:
                if i+j+k == 2020:
                    return i*j*k

print(part2())
