class Interval:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def __contains__(self, item):
        return item.start >= self.start and item.end <= self.end


class Solver:
    def __init__(self, input_data: str, test_data: str):
        self.input = []

        for line in input_data.split('\n'):
            a1, b1 = line.split(',')[0].split('-')
            a2, b2 = line.split(',')[1].split('-')
            self.input.append([
                Interval(a1, b1),
                Interval(a2, b2)
            ])

    def part_a(self):
        count = 0

        for pair in self.input:
            int1, int2 = pair

            if int1 in int2 or int2 in int1:
                count += 1

        return count

    def part_b(self):
        count = 0

        for pair in self.input:
            int1, int2 = pair
            set1 = set(range(int1.start, int1.end+1))
            set2 = set(range(int2.start, int2.end+1))

            if len(set1.intersection(set2)) != 0:
                count += 1

        return count
