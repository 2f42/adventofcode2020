def read_input(fname="input.txt"):
    out = []
    with open(fname) as f:
        for line in f.readlines():
            line = line.strip()
            if "mask" in line:
                bits = line.split("=")[1].replace(" ", "")
                out.append(("mask", bits))
            else:
                mem_loc = int(line[line.index("[")+1:line.index("]")])
                val = int(line.split("=")[1].replace(" ", ""))
                out.append(("mem", mem_loc, val))
    return out

def emulate_version_1(program):
    mem = {}
    andmask = -1
    ormask = 0
    for instr in program:
        if instr[0] == "mask":
            ormask = int(instr[1].replace("X", "0"), 2)
            andmask = int(instr[1].replace("X", "1"), 2)
        elif instr[0] == "mem":
            mem[instr[1]] = instr[2] & andmask | ormask
    return sum(mem[k] for k in mem)

def get_masks(mask):
    nms = [""]
    for i in range(len(mask)):
        if mask[i] == "X":
            nms = list(map(lambda x: x+"0", nms)) + \
                  list(map(lambda x: x+"1", nms))
        else:
            for n in range(len(nms)):
                nms[n] += "1"
    return nms

def emulate_version_2(program):
    mem = {}
    mask = ""
    masks = "0" * 36
    cur = 0
    for instr in program:
        if instr[0] == "mask":
            mask = instr[1]
            masks = [int(m, 2) for m in get_masks(mask)]
        elif instr[0] == "mem":
            # i spent an hour and a half debugging my code
            # it was because i put "0" instead of "1"
            loc = instr[1] | int(mask.replace("X", "1"), 2)
            for l in masks:
                mem[l & loc] = instr[2]
    return sum(mem[k] for k in mem)

inp = read_input()
print(emulate_version_1(inp))
print(emulate_version_2(inp))
