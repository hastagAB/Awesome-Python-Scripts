from sudoku_solver.solver import *

x =    [[8, 1, 0, 0, 3, 0, 0, 2, 7],
        [0, 6, 2, 0, 5, 0, 0, 9, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 6, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 5, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 2, 0, 0, 1, 0, 7, 5, 0],
        [3, 8, 0, 0, 7, 0, 0, 4, 2]]




if __name__ == "__main__":
    print("INPUT => ")
    printsudoku(x)
    solveSudoku(x)
    print("OUTPUT => ")
    printsudoku(x)
