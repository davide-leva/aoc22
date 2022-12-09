class Move:
    def __init__(self, direction, distance):
        self.direction = {
            'R': (0, 1),
            'U': (1, 0),
            'L': (0, -1),
            'D': (-1, 0)
        }[direction]
        self.distance = distance

    def update(self, rope):
        if self.distance > 0:
            rope[0] += self.direction[0]
            rope[1] += self.direction[1]
            self.distance -= 1
            return True
        else:
            return False


class Position:
    def __init__(self, head, tail):
        self.position = []

        vd = head[0] - tail[0]
        hd = head[1] - tail[1]

        if abs(vd) > 0:
            if vd > 0:
                self.position.append(Move('U', abs(vd)))
            else:
                self.position.append(Move('D', abs(vd)))

        if abs(hd) > 0:
            if hd > 0:
                self.position.append(Move('R', abs(hd)))
            else:
                self.position.append(Move('L', abs(hd)))

    def is_near(self):
        for dire in self.position:
            if dire.distance > 1:
                return False

        return True


class Solver:
    def __init__(self, input_data: str, test_data):
        self.input = []

        for line in input_data.split('\n'):
            line = line.split(' ')

            self.input.append([line[0], int(line[1])])

    def part_a(self):
        head = [0, 0]
        tail = [0, 0]

        visited = set()

        for line in self.input:
            move = Move(line[0], line[1])

            while move.update(head):
                position = Position(head, tail)

                if not position.is_near():
                    for component in position.position:
                        component.distance = max(1, component.distance)
                        component.update(tail)

                visited.add(tuple(tail))

        return len(visited)

    def part_b(self):
        rope = []

        for i in range(10):
            rope.append([0, 0])

        visited = set()

        for line in self.input:
            move = Move(line[0], line[1])

            while move.update(rope[0]):
                for i in range(9):
                    position = Position(rope[i], rope[i+1])

                    if not position.is_near():
                        for component in position.position:
                            component.distance = max(1, component.distance)
                            component.update(rope[i+1])

                visited.add(tuple(rope[9]))

        return len(visited)
