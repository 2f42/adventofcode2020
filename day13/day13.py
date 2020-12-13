def read_input(fname="input.txt"):
    out = []
    with open(fname) as f:
        splitlines = f.read().split("\n")
        out.append(int(splitlines[0].strip()))
        out.append([])
        for bus in splitlines[1].split(","):
            if bus != "x":
                out[1].append(int(bus))
            else:
                out[1].append("x")
    return out

def find_earliest_bus(earliest, buses):
    t = earliest
    while True:
        for bus in buses:
            if bus == "x":
                continue
            if not t % bus:
                return (t-earliest) * bus
        t += 1

## calculating the chinese remainder
def find_sequence(buses):
    s = 0
    pr = 1
    rs = []
    for i in range(len(buses)):
        if buses[i] != "x":
            pr *= buses[i]
            rs.append((buses[i], buses[i]-i%buses[i]))
    for n, r in rs:
        a, b = pr // n, n
        x0, x1 = 0, 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += n
        s += r * x1 * pr // n
    return s % pr

inp = read_input()
print("part1:\t", find_earliest_bus(*inp))
print("part2:\t", find_sequence(inp[1]))
