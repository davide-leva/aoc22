import json
import functools

def sgn(x):
    return (x > 0) - (x < 0)


def compare(left, right):
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]

    for i in range(min(len(left), len(right))):
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] > right[i]:
                return -1
            elif left[i] < right[i]:
                return 1
        else:
            comparison = compare(left[i], right[i])
            if comparison != 0:
                return comparison

    return sgn(len(right) - len(left))

class Solver:
    def __init__(self, input_data: str, test_data: str):
        self.input = []
        for pair in input_data.split('\n\n'):
            for packet in pair.split('\n'):
                packet = packet.replace('\n', '')
                self.input.append(json.loads(packet.replace('\'', '"')))

    def part_a(self):
        sum_pair = 0

        for i in range(0, len(self.input), 2):
            left = self.input[i]
            right = self.input[i + 1]

            if compare(left, right) == 1:
                sum_pair += i // 2 + 1

        return sum_pair

    def part_b(self):
        self.input.append([[2]])
        self.input.append([[6]])

        self.input.sort(key=functools.cmp_to_key(compare))
        self.input.reverse()

        decoder_key = ((self.input.index([[2]]) + 1) * (self.input.index([[6]]) + 1))
        print(decoder_key)
        return decoder_key
