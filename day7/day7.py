def read_bag_string(bags):
    k = " ".join(bags.split()[:2])
    others = bags.split("contain")[1]
    cols = {" ".join(bag.split()[1:3]) : int(bag.split()[0]) \
            for bag in others.split(",")}
    return k, cols

def read_input(fname="input.txt"):
    col_rules = {}
    with open(fname) as f:
        for line in f.readlines():
            if "no other bags" in line:
                col_rules[" ".join(line.strip().split()[:2])] = {}
            else:
                k, v = read_bag_string(line.strip())
                col_rules[k] = v
    return col_rules

## pls ignore this, its an actual mess, ill fix later
def search(inp, target="shiny gold"):
    successes = []
    failures = []
    for col in inp:
        cur_cols = [col]
        while True:
            if cur_cols == []:
                failures.append(col)
                break
            if cur_cols[-1] in successes or cur_cols[-1] == target:
                successes += cur_cols[:-1]
                break
            if inp[cur_cols[-1]] == {}:
                failures.append(cur_cols.pop())
                continue
            elif cur_cols[-1] in failures:
                cur_cols.pop()
                continue
            for c2 in inp[cur_cols[-1]]:
                if c2 not in failures:
                    cur_cols.append(c2)
                    break
            else:
                failures.append(cur_cols.pop())
    return len(successes)

def part2(inp, startpoint="shiny gold"):
    total = 1
    for bag in inp[startpoint]:
        total += inp[startpoint][bag] * part2(inp, bag)
    return total

print("part1:\t", search(read_input()))
print("part2:\t", part2(read_input())-1) ## <-- this -1 wasted 15 minutes of my life
