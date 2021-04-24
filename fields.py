class SudokuFields:
    rows = list()
    columns = list()
    squares = list()
    cell_values = dict()
    indexes_of_zeros = list()

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.t_puzzle = list(map(list, zip(*puzzle)))
        i_square = j_square = 0

        for i in range(9):
            self._init_row(i)
            self._init_column(i)
            self._init_square(i_square, j_square)
            self._init_index_of_zero(i)
            if j_square == 6:
                i_square += 3
                j_square = 0
            else:
                j_square += 3

        self._init_cell_values()

    def _init_row(self, i):
        row = set(self.puzzle[i])
        row.discard(0)
        self.rows.append(row)

    def _init_column(self, i):
        column = set(self.t_puzzle[i])
        column.discard(0)
        self.columns.append(column)

    def _init_square(self, i_square, j_square):
        square = set(self.puzzle[i][j] for i in range(i_square, i_square + 3) for j in range(j_square, j_square + 3))
        square.discard(0)
        self.squares.append(square)

    def _init_index_of_zero(self, i):
        index_of_zero = list((i, j) for j in range(9) if self.puzzle[i][j] == 0)
        self.indexes_of_zeros.extend(index_of_zero)

    def _init_cell_values(self):
        for i, j in self.indexes_of_zeros:
            unavailable_values = self.rows[i] | self.columns[j] | self.squares[i // 3 * 3 + j // 3]
            self.cell_values[(i, j)] = set(range(1, 10)) - unavailable_values








