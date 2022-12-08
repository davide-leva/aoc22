def is_unique(string: str):
    for element in string:
        if string.count(element) != 1:
            return False

    return True


class Solver:
    def __init__(self, input_data: str, test_data):
        self.input = input_data

    def part_a(self):
        for i in range(4, len(self.input)):
            if is_unique(self.input[i-4:i]):
                return i

    def part_b(self):
        for i in range(14, len(self.input)):
            if is_unique(self.input[i-14:i]):
                return i
