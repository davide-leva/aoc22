class Solver:
    def __init__(self, input_data):
        self.input = []

        for chunk in input_data.split('\n\n'):
            self.input.append([int(x) for x in chunk.split('\n')])

    def part_a(self):
        elves = self.input

        most = 0
        for elf in elves:
            most = max(sum(elf), most)

        return most

    def part_b(self):
        elves = self.input

        elves.sort(key=lambda elf: sum(elf), reverse=True)
        return sum(elves[0] + elves[1] + elves[2])
