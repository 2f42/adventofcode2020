from copy import deepcopy

def read_input(fname="input.txt"):
    out = []
    with open(fname) as f:
        for line in f.readlines():
            out.append(list(line.strip()))
    return out

def count_adjacent(seats, w, h, x, y):
    count = 0
    for i in range(3):
        if x+i-1 < 0 or x+i-1 >= w:
            continue
        for j in range(3):
            if y+j-1 < 0 or y+j-1 >= h or (i==1 and j==1):
                continue
            count += 1 if seats[y+j-1][x+i-1] == "#" else 0
    return count

def can_see_occupied(seats, w, h, x, y, mx, my):
    x += mx
    y += my
    while w > x >= 0 and h > y >= 0:
        if seats[y][x] == "#":
            return 1
        if seats[y][x] == "L":
            return 0
        x += mx
        y += my
    return 0

def count_blockers(seats, w, h, x, y):
    count = 0
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            count += can_see_occupied(seats, w, h, x, y, i-1, j-1)
    return count

def find_stability(seats, leave, counter):
    new_seats = deepcopy(seats)
    old_seats = []
    height = len(seats)
    width = len(seats[0])
    while old_seats != new_seats:
        old_seats = deepcopy(new_seats)
        new_seats = [[] for y in range(height)]
        for y in range(height):
            for x in range(width):
                if old_seats[y][x] == ".":
                    new_seats[y].append(".")
                    continue
                count = counter(old_seats, width, height, x, y)
                if count == 0 and old_seats[y][x] == "L":
                    new_seats[y].append("#")
                elif count >= leave and old_seats[y][x] == "#":
                    new_seats[y].append("L")
                else:
                    new_seats[y].append(old_seats[y][x])
    return sum(l.count("#") for l in new_seats)

inp = read_input("input.txt")
print("part1:\t", find_stability(inp, 4, count_adjacent))
print("part2:\t", find_stability(inp, 5, count_blockers))
## runs a bit slow
