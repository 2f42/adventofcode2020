# made after the original day12.py
# this solution feels nicer to me, idk why

class Ship:

    def __init__(self, start, waypoint, fname="input.txt"):
        self._pos = start
        self._waypoint = waypoint
        self._instructions = []
        with open(fname) as f:
            for line in f.readlines():
                line = line.strip()
                self._instructions.append((line[0], int(line[1:])))

    _actions = {}

    def __call__(self):
        for i in self._instructions:
            self._actions[i[0]](self, i[1])
        return sum(abs(c) for c in self._pos)

    def rotate_waypoint(self, n):
        for i in range(n):
            self._waypoint = [self._waypoint[1], -self._waypoint[0]]
    def move_waypoint(self, x, y):
        self._waypoint[0] += x
        self._waypoint[1] += y

    def move_ship(self, x, y):
        self._pos[0] += x
        self._pos[1] += y

    def move_towards_waypoint(self, n):
        self.move_ship(self._waypoint[0]*n, self._waypoint[1]*n)


class Part1(Ship):

    def __init__(self, fname="input.txt"):
        super().__init__([0,0], [1,0], fname)

    _actions = {\
        "N": lambda self, a: self.move_ship(0,  a),
        "S": lambda self, a: self.move_ship(0, -a),
        "E": lambda self, a: self.move_ship( a, 0),
        "W": lambda self, a: self.move_ship(-a, 0),
        "F": lambda self, a: self.move_towards_waypoint(a),
        "R": lambda self, a: self.rotate_waypoint(a//90),
        "L": lambda self, a: self.rotate_waypoint(4-(a//90)%4)
    }

class Part2(Ship):

    def __init__(self, fname="input.txt"):
        super().__init__([0,0], [10,1], fname)

    _actions = {\
        "N": lambda self, a: self.move_waypoint(0,  a),
        "S": lambda self, a: self.move_waypoint(0, -a),
        "E": lambda self, a: self.move_waypoint( a, 0),
        "W": lambda self, a: self.move_waypoint(-a, 0),
        "F": lambda self, a: self.move_towards_waypoint(a),
        "R": lambda self, a: self.rotate_waypoint(a//90),
        "L": lambda self, a: self.rotate_waypoint(4-(a//90)%4)
    }

print("part1:\t", Part1()())
print("part2:\t", Part2()())
