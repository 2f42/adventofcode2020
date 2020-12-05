def read_input(filename="input.txt"):
    out = []
    with open(filename) as f:
        for line in f.readlines():
            out.append(line.strip())
    return out

def traverse(treemap, mx, my):
    max_x = len(treemap[0])
    max_y = len(treemap)-1
    x, y = 0, 0
    trees = 0
    while y < max_y:
        x = (x+mx) % max_x
        y += my
        if treemap[y][x] == "#":
            trees += 1
    return trees

def traverse_slopes(treemap, *slopes):
    out = 1
    for slope in slopes:
        out *= traverse(treemap, *slope)
    return out

print(traverse_slopes(read_input(), (1,1), (3,1), (5,1), (7,1), (1,2)))
