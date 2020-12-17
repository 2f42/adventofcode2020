class ConwayCube:

    def __init__(self, dims, fname="input.txt"):
        self._fname = fname
        self._dims = dims
        self.cur_state = set()
        with open(fname) as f:
            i = 0
            for line in f.readlines():
                if line != "":
                    for c in range(len(line)):
                        if line[c] == "#":
                            self.cur_state.add(\
                                tuple([c, i] + [0 for _ in range(dims-2)]))
                    i += 1

    def __call__(self, n):
        for i in range(n):
            self.update()
        return len(self.cur_state)

    def count_neighbours(self, *args):
        count = 0
        cur_offs = [-1 for i in range(self._dims)]
        skip = [0 for i in range(self._dims)]
        d = 0
        while cur_offs[-1] < 2:
            if cur_offs != skip:
                c = tuple(cur_offs[i] + args[i] for i in range(self._dims))
                count += 1 if c in self.cur_state else 0
            cur_offs[d] += 1
            while cur_offs[d] > 1 and d < self._dims-1:
                cur_offs[d] = -1
                d += 1
                cur_offs[d] += 1
            d = 0
        return count

    def update(self):
        new_state = set()
        ranges = [\
            (min(i[d] for i in self.cur_state)-1, \
             max(i[d] for i in self.cur_state)+2) \
                for d in range(self._dims)]
        curpos = [ranges[i][0] for i in range(self._dims)]
        d = 0
        while curpos[-1] <= ranges[-1][1]:
            n = self.count_neighbours(*curpos)
            t = tuple(curpos)
            if t in self.cur_state:
                if n == 2 or n == 3:
                    new_state.add(t)
            else:
                if n == 3:
                    new_state.add(t)
            curpos[d] += 1
            while curpos[d] >= ranges[d][1] and d < self._dims-1:
                curpos[d] = ranges[d][0]
                d += 1
                curpos[d] += 1
            d = 0
        self.cur_state = new_state

print("part1:\t", ConwayCube(3)(6))
print("part2:\t", ConwayCube(4)(6)) ## a bit slow
