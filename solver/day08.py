def is_visible(forest, tree):
    height = forest[tree[0]][tree[1]]
    column = [line[tree[1]] for line in forest]
    row = forest[tree[0]]

    row_before = row[:tree[1] + 1]
    max_row_before = max(row_before)
    count_row_before = row_before.count(max_row_before)

    row_after = row[tree[1]:]
    max_row_after = max(row_after)
    count_row_after = row_after.count(max_row_after)

    column_before = column[:tree[0] + 1]
    max_column_before = max(column_before)
    count_column_before = column_before.count(max_column_before)

    column_after = column[tree[0]:]
    max_column_after = max(column_after)
    count_column_after = column_after.count(max_column_after)

    visible_left = height == max_row_before and count_row_before == 1
    visible_right = height == max_row_after and count_row_after == 1
    visible_top = height == max_column_before and count_column_before == 1
    visible_down = height == max_column_after and count_column_after == 1

    return visible_left or visible_right or visible_top or visible_down


def scenic_score(forest, tree):
    height = forest[tree[0]][tree[1]]
    score = 1

    count = 0
    for i in range(tree[0]-1, -1, -1):
        count += 1

        if forest[i][tree[1]] >= height:
            break

    score *= count

    count = 0
    for i in range(tree[0]+1, len(forest[0])):
        count += 1

        if forest[i][tree[1]] >= height:
            break

    score *= count

    count = 0
    for i in range(tree[1]-1, -1, -1):
        count += 1

        if forest[tree[0]][i] >= height:
            break

    score *= count

    count = 0
    for i in range(tree[1]+1, len(forest[tree[0]]), 1):
        count += 1

        if forest[tree[0]][i] >= height:
            break

    score *= count

    return score


class Solver:
    def __init__(self, input_data: str, test_data):
        self.input = []

        for line in input_data.split('\n'):
            self.input.append([int(x) for x in line])

        self.ROW = len(self.input)
        self.COLUMN = len(self.input)

    def part_a(self):
        visible_tree = 0
        outside_tree = 4 * (self.ROW - 1)

        for i in range(1, self.ROW - 1):
            for j in range(1, self.COLUMN - 1):
                if is_visible(self.input, (i, j)):
                    visible_tree += 1

        return outside_tree + visible_tree

    def part_b(self):
        best_score = 0

        for i in range(1, self.ROW - 1):
            for j in range(1, self.COLUMN -1):
                best_score = max(scenic_score(self.input, (i, j)), best_score)

        return best_score
