def move_element(towers: list, quantity: int, from_tower: int, to_tower: int):
    if quantity == 0:
        return

    towers[to_tower - 1].append(towers[from_tower - 1].pop())
    move_element(towers, quantity - 1, from_tower, to_tower)


def move_tower(towers: list, quantity: int, from_tower: int, to_tower: int):
    sub_tower = towers[from_tower - 1][-quantity:]

    towers[to_tower - 1].extend(sub_tower)
    towers[from_tower - 1] = towers[from_tower - 1][:-quantity]


class Solver:
    def __init__(self, input_data: str, test_data: str):
        towers = []
        self.towers = []
        self.moves = []

        for i in range(8):
            line = input_data.split('\n')[i]
            towers.append([line[j] for j in range(1, 36, 4)])

        for i in range(9):
            self.towers.append([])
            for j in range(8):
                if towers[j][i] != ' ':
                    self.towers[i].append(towers[j][i])
            self.towers[i].reverse()

        for line in input_data.split('\n')[10:]:
            args = line.split(' ')
            self.moves.append((int(args[1]), int(args[3]), int(args[5])))

    def part_a(self):
        towers = self.towers.copy()
        moves = self.moves.copy()

        for move in moves:
            move_element(towers, move[0], move[1], move[2])

        return ''.join([x[-1] for x in towers])

    def part_b(self):
        towers = self.towers.copy()
        moves = self.moves.copy()

        for move in moves:
            move_tower(towers, move[0], move[1], move[2])

        print(''.join([x[-1] for x in towers]))

        return ''.join([x[-1] for x in towers])
