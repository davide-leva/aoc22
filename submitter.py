from aocd.exceptions import PuzzleLockedError
from aocd.models import Puzzle
from datetime import date
from rich import print

YEAR = date.today().year
DAY = date.today().day


def create_solver(i):
    with open('solver/template.txt', 'r') as template:
        with open(f'solver/day{i:02}.py', 'w') as solver_file:
            solver_file.write(template.read())


print(f'[bold yellow]-----| Advent of Code {YEAR} by Davivelex |-----[/]\n')

for day in range(1, DAY + 1):
    puzzle = 0

    try:
        puzzle = Puzzle(YEAR, day)
        Solver = __import__(f'solver.day{day:02}', fromlist=['Solver']).Solver
        solver = Solver(puzzle.input_data)

        print(f'[bold green]--- Day {day}: [link={puzzle.url}]{puzzle.title}[/link] ---[/]', )

        if not puzzle.answered_a and solver.part_a() != NotImplemented:
            puzzle.answer_a = solver.part_a()

        if not puzzle.answered_b and solver.part_b() != NotImplemented:
            puzzle.answer_b = solver.part_b()

        print(f' * Part A: {puzzle.answer_a}')
        print(f' * Part B: {puzzle.answer_b}\n')

    except PuzzleLockedError as e:
        print(f'[red](!) Error: {e}\n[/]')

    except ModuleNotFoundError as e:
        create_solver(day)
        print(f'[red](!) Error: {e}, creating new solver...[/]\n')

    except AttributeError as e:
        part = e.name.split("_")[1].upper()
        if part == 'A':
            puzzle.view()

        print(f' * Part {part}: --- ')
