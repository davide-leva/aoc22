POINT = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3
    },
    'X': 1,
    'Y': 2,
    'Z': 3
}


class Solver:
    def __init__(self, input_data, test_data):
        self.input = []

        for line in input_data:
            self.input.append([str(x) for x in line.replace('\n', '').split(' ')])

    def part_a(self):
        games = self.input

        points = 0
        for game in games:
            player1, player2 = game

            points += POINT[player1][player2] + POINT[player2]

        return points

    def part_b(self):
        games = self.input

        points = 0
        for game in games:
            player1, player2 = game

            if player2 == 'X':
                for p2, value in POINT[player1].items():
                    if value == 0:
                        points += POINT[p2]
            elif player2 == 'Y':
                for p2, value in POINT[player1].items():
                    if value == 3:
                        points += POINT[p2] + 3
            else:
                for p2, value in POINT[player1].items():
                    if value == 6:
                        points += POINT[p2] + 6

        return points
