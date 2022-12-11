class Solver:
    def __init__(self, input_data: str, test_data: str):
        self.input = []
        self.position = [[0, [0, 1, 2]]]
        self.crt = []

        for _ in range(6):
            self.crt.append(['.'] * 40)

        for line in input_data.split('\n'):
            line = line.split(' ')
            self.input.append(['noop', 0])

            if line[0] != 'noop':
                self.input.append(['add', int(line[1])])

    def part_a(self):
        register = 1
        signal = 0

        for cycle, operation in enumerate(self.input):
            op_type, value = operation

            if op_type == 'add':
                register += value

            self.position.append([cycle+1, [register-1, register, register+1]])

            if cycle in [18, 58, 98, 138, 178, 218]:
                signal += (cycle+2) * register

        return signal

    def part_b(self):
        self.part_a()
        self.position.pop()

        for pos, sprite in self.position:
            row = pos // 40
            column = pos % 40

            if column in sprite:
                self.crt[row][column] = '#'

        for line in self.crt:
            print(''.join(line))

        return 'ZFBFHGUP'
