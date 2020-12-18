def read_input(fname="input.txt"):
    out = []
    with open(fname) as f:
        for line in f.readlines():
            line = line.strip()
            out.append(line)
    return out

ops = {
    "+": (lambda x, y: (x or 0)+y, 0),
    "*": (lambda x, y: (x or 1)*y, 1)
}

def to_rpn(s, cares=True):
    out = []
    opstack = []
    for c in s:
        if c in "0123456789":
            out.append(c)
        elif c in ops:
            while opstack and opstack[-1] != "(" \
                    and (ops[opstack[-1]][1] < ops[c][1] or not cares):
                out.append(opstack.pop())
            opstack.append(c)
        elif c == "(":
            opstack.append(c)
        elif c == ")":
            while opstack and opstack[-1] != "(":
                out.append(opstack.pop())
            if opstack[-1] == "(":
                opstack.pop()
    while opstack:
        out.append(opstack.pop())
    return out

def process_rpn(rpn):
    stack = []
    rpn = list(reversed(rpn))
    while rpn:
        if rpn[-1] in ops:
            stack.append(ops[rpn.pop()][0](int(stack.pop()), int(stack.pop())))
        elif rpn[-1] in "0123456789":
            stack.append(rpn.pop())
    return stack[0]

inp = read_input()
print("part1:\t", sum(map(process_rpn, map(lambda s: to_rpn(s, False), inp))))
print("part2:\t", sum(map(process_rpn, map(to_rpn, inp))))
