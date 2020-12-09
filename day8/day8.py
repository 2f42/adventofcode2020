class Computer:

    opcodes = {}

    def __init__(self):
        self.times_run = 0
        self.instructions = []
        self.halt_at = 0

    def __iter__(self):
        self.times_run += 1
        self.accumulator = 0
        self.pointer = 0
        self.visited = set()
        return self

    def __next__(self):
        if self.isdone():
            raise StopIteration
        self.visited.add(self.pointer)
        opcode = self.instructions[self.pointer][0]
        arg = self.instructions[self.pointer][1]
        self.opcodes[opcode](self, arg)
        self.pointer += 1

    def read_input(self, fname="input.txt"):
        self.instructions = []
        with open(fname) as f:
            for line in f.readlines():
                instr = line.strip().split()
                self.instructions.append([instr[0], int(instr[1])])
        self.halt_at = len(self.instructions)
        self.times_run = 0
        return self

    def isdone(self):
        return self.pointer in self.visited or self.pointer >= self.halt_at

    def attempt_repair(self):
        for i in range(len(self.instructions)):
            original = self.instructions[i][0]
            if   original == "jmp": self.instructions[i][0] = "nop"
            elif original == "nop": self.instructions[i][0] = "jmp"
            for c in self:
                pass
            if self.pointer >= len(self.instructions):
                return self.accumulator
            self.instructions[i][0] = original

    def _nop(self, arg):
        return
    opcodes["nop"] = _nop

    def _acc(self, arg):
        self.accumulator += arg
    opcodes["acc"] = _acc

    def _jmp(self, arg):
        self.pointer += arg-1
    opcodes["jmp"] = _jmp

handheld_console = Computer()
for c in handheld_console.read_input():
    pass
print(handheld_console.accumulator)
print(handheld_console.attempt_repair())
