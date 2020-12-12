def read_input(fname="input.txt"):
    out = []
    with open(fname) as f:
        for line in f.readlines():
            out.append((line[0], int(line.strip()[1:])))
    return out

dirs = [(1,0), (0,-1), (-1,0), (0,1)]

def modify_ship(ship, action, amount):
    if action == "N":
        ship[2] += amount
    elif action == "S":
        ship[2] -= amount
    elif action == "E":
        ship[1] += amount
    elif action == "W":
        ship[1] -= amount
    elif action == "F":
        ship[1] += dirs[ship[0]][0] * amount
        ship[2] += dirs[ship[0]][1] * amount
    elif action == "L":
        ship[0] = (ship[0]-(amount//90))%4
    elif action == "R":
        ship[0] = (ship[0]+(amount//90))%4
    return ship

def find_new_pos(instructions):
    ship = [0, 0, 0]
    for i in instructions:
        ship = modify_ship(ship, *i)
    return abs(ship[1]) + abs(ship[2])

def modify_waypoint(waypoint, action, amount):
    if action == "N":
        waypoint[1] += amount
    elif action == "S":
        waypoint[1] -= amount
    elif action == "E":
        waypoint[0] += amount
    elif action == "W":
        waypoint[0] -= amount
    elif action == "L":
        for i in range(amount//90):
            waypoint = [-waypoint[1], waypoint[0]]
    elif action == "R":
        for i in range(amount//90):
            waypoint = [waypoint[1], -waypoint[0]]
    return waypoint

def find_new_pos2(instructions):
    waypoint = [10, 1]
    ship = [0, 0]
    for i in instructions:
        if i[0] == "F":
            ship[0] += waypoint[0] * i[1]
            ship[1] += waypoint[1] * i[1]
        else:
            waypoint = modify_waypoint(waypoint, *i)
    return abs(ship[0]) + abs(ship[1])

inp = read_input("input.txt")
print("part1:\t", find_new_pos(inp))
print("part2:\t", find_new_pos2(inp))
