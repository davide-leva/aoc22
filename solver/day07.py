import json


def add_file(fs: dict, path, file):
    for dir_path in path:
        if dir_path in fs.keys():
            fs = fs.get(dir_path)
        else:
            fs[dir_path] = {
                '__files__': []
            }
            fs = fs[dir_path]

    if file[0] == 'dir':
        fs[file[1]] = {
            '__files__': []
        }
    else:
        fs['__files__'].append(int(file[0]))

    return fs


def visit(fs: dict):
    sum_size = 0

    for key in fs:
        if key == '__files__':
            sum_size += sum(fs[key])
        elif key != '__size__':
            visit(fs[key])
            sum_size += fs[key]['__size__']

    fs['__size__'] = sum_size


def get_dir_a(fs: dict, collector: list):
    if fs['__size__'] <= 100000:
        collector.append(fs)

    for key in fs:
        if key not in ['__files__', '__size__']:
            get_dir_a(fs[key], collector)


def get_dir_b(fs: dict, collector: list, minimum):
    if fs['__size__'] >= minimum:
        collector.append(fs)

    for key in fs:
        if key not in ['__files__', '__size__']:
            get_dir_b(fs[key], collector, minimum)


class Solver:
    def __init__(self, input_data: str, test_data: str):
        self.input = {}
        path = []

        for line in input_data.split('\n'):
            command = line.split(' ')

            if command[0] == '$':
                if command[1] == 'cd':
                    if command[2] == '..':
                        path.pop()
                    else:
                        path.append(command[2])
            else:
                add_file(self.input, path, command)

    def part_a(self):
        visit(self.input['/'])
        can_delete = []
        get_dir_a(self.input['/'], can_delete)

        return sum(map(lambda file: file['__size__'], can_delete))

    def part_b(self):
        visit(self.input)
        can_delete = []
        get_dir_b(self.input['/'], can_delete, self.input['/']['__size__'] - 4e7)

        return min(map(lambda x: x['__size__'], can_delete))
