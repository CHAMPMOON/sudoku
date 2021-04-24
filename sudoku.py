from fields import SudokuFields
from solver import SudokuSolver
from print import SudokuPrinter


class Sudoku:
    @staticmethod
    def create(puzzle):
        return SudokuFields(puzzle)

    @staticmethod
    def solve(fields):
        solver = SudokuSolver(fields)
        next(solver.solve(), False)

    @staticmethod
    def print(fields):
        SudokuPrinter.print(fields.puzzle)
