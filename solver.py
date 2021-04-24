from fields import SudokuFields


class SudokuSolver:
    def __init__(self, fields: SudokuFields):
        self.rows = fields.rows
        self.columns = fields.columns
        self.squares = fields.squares
        self.cell_values = fields.cell_values
        self.indexes_of_zeros = fields.indexes_of_zeros
        self.puzzle = fields.puzzle

    def solve(self, step=0):
        if step == len(self.indexes_of_zeros):
            yield self.puzzle

        i, j = self.indexes_of_zeros[step]
        square_index = i // 3 * 3 + j // 3

        for elem in self.cell_values.get((i, j)):
            if elem not in self.rows[i] and elem not in self.columns[j] and elem not in self.squares[square_index]:
                self._add_element((i, j), elem)
                yield from self.solve(step + 1)
                self._delete_element((i, j), elem)

    def _add_element(self, index, element):
        i, j = index
        square_index = i // 3 * 3 + j // 3
        self.rows[i].add(element)
        self.columns[j].add(element)
        self.squares[square_index].add(element)
        self.puzzle[i][j] = element

    def _delete_element(self, index, element):
        i, j = index
        square_index = i // 3 * 3 + j // 3
        self.rows[i].discard(element)
        self.columns[j].discard(element)
        self.squares[square_index].discard(element)
        self.puzzle[i][j] = 0