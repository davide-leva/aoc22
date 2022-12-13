from math import prod


class Monkey:
    def __init__(self, starting_items: list, operation, throw):
        self.items = starting_items
        self.inspected_items = 0
        self.mod = throw[0]

        if operation[1] == 'old':
            self.operation = lambda item: item ** 2
        elif operation[0] == '+':
            self.operation = lambda item: item + int(operation[1])
        elif operation[0] == '*':
            self.operation = lambda item: item * int(operation[1])

        self.test = lambda item: throw[1] if item % throw[0] == 0 else throw[2]

    def inspect_factor_3(self, index):
        self.inspected_items += 1
        self.items[index] = self.operation(self.items[index])//3

    def inspect_mod(self, index, mod):
        self.inspected_items += 1
        self.items[index] = self.operation(self.items[index]) % mod

    def receive(self, item):
        self.items.append(item)

    def throw(self, monkeys, index):
        item = self.items[index]
        monkeys[self.test(item)].receive(item)


class Solver:
    def __init__(self, input_data: str, test_data: str):
        self.input = []

        for monkey_data in input_data.split('\n\n'):
            monkey_data = monkey_data.split('\n')

            items = [int(n) for n in monkey_data[1].split(': ')[1].split(', ')]
            operation = monkey_data[2].split(' ')[-2:]
            throw = [int(n) for n in [
                monkey_data[3].split(' ')[-1],
                monkey_data[4].split(' ')[-1],
                monkey_data[5].split(' ')[-1]]]

            self.input.append(Monkey(items, operation, throw))

    def print(self, m):
        for i, mon in enumerate(m):
            print(f'Monkey {i}: inspected {mon.inspected_items} items')

    def part_a(self):
        monkeys = self.input.copy()

        for _ in range(300):
            for monkey in monkeys:
                for i in range(len(monkey.items)):
                    monkey.inspect_factor_3(i)
                    monkey.throw(monkeys, i)

                monkey.items.clear()

        sorted_monkey = sorted(monkeys, key=lambda x: x.inspected_items, reverse=True)
        monkey_business = sorted_monkey[0].inspected_items * sorted_monkey[1].inspected_items

        print(monkey_business)
        return monkey_business

    def part_b(self):
        monkeys = self.input.copy()

        mod = prod([monkey.mod for monkey in monkeys])

        for _ in range(10000):
            for monkey in monkeys:
                for i in range(len(monkey.items)):
                    monkey.inspect_mod(i, mod)
                    monkey.throw(monkeys, i)

                monkey.items.clear()

        sorted_monkey = sorted(monkeys, key=lambda x: x.inspected_items, reverse=True)
        monkey_business = sorted_monkey[0].inspected_items * sorted_monkey[1].inspected_items

        return monkey_business
