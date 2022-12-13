MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def search(height_map, starting_pos, destination_pos):
    path_length = [[0 for _ in range(len(height_map[0]))] for __ in range(len(height_map))]
    visited = set()
    visit = [starting_pos]

    while len(visit) > 0:
        cell = visit[0]
        visit.pop(0)

        if cell == destination_pos:
            return path_length[cell[0]][cell[1]]

        for move in MOVES:
            next_cell = (cell[0] + move[0], cell[1] + move[1])
            if 0 <= next_cell[0] < len(height_map) and 0 <= next_cell[1] < len(height_map[0]):
                if height_map[next_cell[0]][next_cell[1]] - height_map[cell[0]][cell[1]] <= 1:
                    if next_cell not in visited:
                        visit.append(next_cell)
                        visited.add(next_cell)
                        path_length[next_cell[0]][next_cell[1]] = path_length[cell[0]][cell[1]] + 1


class Solver:
    def __init__(self, input_data: str, test_data: str):
        self.input = []
        self.visited = {}

        for line in input_data.split('\n'):
            self.input.append(list(line))

        for i in range(len(self.input)):
            for j in range(len(self.input[i])):
                cell = self.input[i][j]
                self.visited[(i, j)] = 99999

                if cell == 'E':
                    self.input[i][j] = 25
                    self.destination = (i, j)
                elif cell == 'S':
                    self.input[i][j] = 0
                    self.start = (i, j)
                    self.visited[(i, j)] = 0
                else:
                    self.input[i][j] = ord(cell) - ord('a')

    def part_a(self):
        return search(self.input, self.start, self.destination)

    def part_b(self):
        path_length = []

        for i in range(len(self.input)):
            for j in range(len(self.input[i])):
                if self.input[i][j] == 0:
                    path_length.append(search(self.input, (i, j), self.destination))

        return min(list(filter(lambda x: x is not None, path_length)))
