def get_seat_vals(seatstr):
    sid = 0
    for c in seatstr:
        sid <<= 1
        sid |= c in "BR"
    return sid

def read_input(fname="input.txt"):
    out = []
    with open(fname) as f:
        for line in f.readlines():
            out.append(get_seat_vals(line.strip()))
    return out

def find_missing():
    inp = read_input()
    max_seat = max(inp)
    for i in range(max_seat):
        if i not in inp and i-1 in inp and i+1 in inp:
            return i

print(find_missing())
