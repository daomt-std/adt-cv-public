import os

import numpy as np


class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, file_path: str) -> None:

        # list of lists (rows)
        loaded_rows: list[list[int]] = []
        # TODO implement loading of the file
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                split_line = line.split(";")
                tmp: list[int] = []
                for i in split_line:
                    tmp.append(int(i.strip()))
                loaded_rows.append(tmp)

        # convert nested list to numpy array
        self.field = np.array(loaded_rows)



    def check_sequence(self, sequence: np.ndarray) -> bool:
        non_zero = sequence[sequence != 0]
        return len(set(non_zero)) == len(non_zero)


    def check_row(self, row_index: int) -> bool:
        row = self.field[row_index:row_index + 1, 0:]
        return self.check_sequence(row)

    def check_column(self, column_index: int) -> bool:
        column = self.field[0:, column_index:column_index+1]
        return self.check_sequence(column)

    def check_block(self, row_index: int, column_index: int) -> bool:
        row_start_index = (row_index // 3) * 3
        column_start_index = (column_index // 3) * 3

        return self.check_sequence(self.field[row_start_index:row_start_index+3, column_start_index:column_start_index+3].reshape(-1))


    def check_one_cell(self, row_index: int , column_index: int) -> bool:
        return self.check_row(row_index) and self.check_column(column_index)

    def get_empty_cell(self) -> tuple[int, int] | None:
        """ Gets the coordinates of the next empty field. """
        for row in range(self.field.shape[0]):
            for col in range(self.field.shape[1]):
                if self.field[row, col] == 0:
                    return (row, col)
        return None

    def solve(self) -> bool:
        """ Recursively solves the sudoku. """
        empty_cell = self.get_empty_cell()
        if empty_cell is None:
            return True
        row, col = empty_cell
        for i in range(1, 10):
            self.field[row, col] = i
            if self.check_one_cell(row, col) and self.solve():
                return True
        self.field[row, col] = 0
        return False





def main() -> None:
    sudoku_solver = SudokuSolver()
    sudoku_solver.load("07-backtracking/sudoku.csv")
    print(sudoku_solver.field)
    """
    for col in range(9):
        for row in range(9):
            print(f"({col}, {row}): {sudoku_solver.check_one_cell(row,col)}")
    """
    sudoku_solver.solve()
    print(sudoku_solver.field)

if __name__ == "__main__":
    main()
