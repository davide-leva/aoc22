def get_duplicate(part1: str, part2: str):
    for element in part1:
        if element in part2:
            return element

    return None


def get_priority(element: str):
    if element.islower():
        return ord(element) - ord('a') + 1
    else:
        return ord(element) - ord('A') + 27


def get_badge(elf1: str, elf2: str, elf3: str):
    for element in elf1:
        if element in elf2 and element in elf3:
            return element

    return None


class Solver:
    def __init__(self, data, test):
        self.input = []

        for line in data.split('\n'):
            self.input.append(line.replace('\n', ''))

    def part_a(self):
        sum_priorities = 0

        for rucksack in self.input:
            size = len(rucksack)
            part1 = rucksack[:size // 2]
            part2 = rucksack[size // 2:]

            duplicate = get_duplicate(part1, part2)
            sum_priorities += get_priority(duplicate)

        return sum_priorities

    def part_b(self):
        sum_priorities = 0

        for i in range(0, len(self.input), 3):
            elf1, elf2, elf3 = self.input[i:i + 3]
            badge = get_badge(elf1, elf2, elf3)
            sum_priorities += get_priority(badge)

        return sum_priorities
