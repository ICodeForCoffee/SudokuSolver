from SudokuSolver import SudokuSolver
from SudokuPuzzle import SudokuPuzzle
import pytest

def test_basic_solving():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver()
    
    # The missing value here is 6.
    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, ' ', 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

    assert puzzle.is_solved() == False
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.squares[3][4]['value'] == 6
    assert puzzle.is_solved() == True

    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, ' ', 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

def test_simple_solving():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver()
    
    #This is the same Matrix from sudoku-puzzle1.txt
    matrix = [
        [' ',' ', 2 , 7 ,' ',' ', 1 , 5 , 6 ],
        [' ', 3 ,' ', 6 , 2 , 8 ,' ', 4 ,' '],
        [ 7 , 6 , 9 ,' ',' ',' ',' ', 3 ,' '],
        [ 9 ,' ', 7 ,' ', 4 , 5 , 3 ,' ',' '],
        [' ',' ',' ',' ', 8 ,' ', 7 , 2 ,' '],
        [ 6 , 2 ,' ', 3 ,' ',' ', 5 ,' ',' '],
        [' ', 5 ,' ', 1 ,' ', 3 ,' ',' ', 9 ],
        [' ', 7 ,' ',' ', 9 ,' ', 2 ,' ', 5 ],
        [ 4 ,' ', 1 , 5 , 7 ,' ',' ',' ',' ']
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

    
    assert puzzle.is_solved() == False
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True
    assert puzzle.guessing_used == False

def test_complex_solving_one():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver()
    
    # This is the same Matrix from sudoku-puzzle6.txt
    matrix = [
        [' ',' ',' ',' ',' ',' ', 1 , 6 ,' '],
        [ 6 ,' ',' ', 3 ,' ',' ', 4 ,' ',' '],
        [' ',' ', 9 ,' ',' ', 7 ,' ',' ',' '],
        [' ',' ', 8 ,' ',' ', 4 ,' ',' ',' '],
        [' ',' ', 2 ,' ',' ',' ',' ',' ', 7 ],
        [' ', 9 ,' ', 8 ,' ',' ', 2 , 5 ,' '],
        [' ', 2 ,' ',' ', 1 , 8 ,' ',' ',' '],
        [' ',' ',' ',' ', 9 ,' ',' ',' ',' '],
        [ 4 , 7 ,' ',' ',' ',' ',' ',' ', 1 ]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

    
    assert puzzle.is_solved() == False
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True

def test_complex_solving_two():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver()
    
    # This is the same Matrix from sudoku-puzzle4.txt with two values filled in
    matrix = [
        [' ',' ',' ',' ',' ', 4 , 3 ,' ',' '],
        [' ', 7 , 5 ,' ', 9 , 8 ,' ',' ', 2 ],
        [' ',' ',' ',' ',' ', 1 ,' ',' ',' '],
        [' ',' ',' ', 6 , 3 ,' ',' ',' ',' '],
        [ 2 , 6 ,' ',' ',' ',' ',' ',' ', 5 ],
        [' ', 9 , 8 , 5 ,' ',' ',' ',' ', 4 ],
        [ 6 , 8 ,' ',' ',' ',' ', 4 ,' ',' '],
        [ 1 , 2 ,' ',' ',' ',' ', 7 , 8 ,' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

    
    assert puzzle.is_solved() == False
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True

def test_analysis_method():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver()
    
    # This is the same Matrix from sudoku-puzzle4.txt with two values filled in
    matrix = [
        [' ', 1 ,' ',' ',' ', 4 , 3 ,' ',' '],
        [' ', 7 , 5 , 3 , 9 , 8 ,' ',' ', 2 ],
        [' ',' ',' ',' ',' ', 1 ,' ',' ',' '],
        [' ',' ',' ', 6 , 3 ,' ',' ',' ',' '],
        [ 2 , 6 ,' ',' ',' ',' ',' ',' ', 5 ],
        [' ', 9 , 8 , 5 ,' ',' ',' ',' ', 4 ],
        [ 6 , 8 ,' ',' ',' ',' ', 4 ,' ',' '],
        [ 1 , 2 ,' ',' ',' ',' ', 7 , 8 ,' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

    assert puzzle.is_solved() == False
    
    # Check that analysis calculates the value at 7, 4
    instance.populate_possible_values(puzzle)
    assert puzzle.squares[7][4]['value'] == ' '
    assert len(puzzle.squares[7][4]['possible_values']) == 3
    change_made = instance.perform_analysis(puzzle, 7, 4)
    assert change_made == True
    
    instance.promote_solved_squares(puzzle)
    assert puzzle.squares[7][4]['value'] == 4
    
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True

def test_load_function():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver()
    
    puzzle = instance.load_puzzle("SudokuPuzzles\\sudoku-puzzle1.txt")
    
    # This is the same Matrix from sudoku-puzzle1.txt
    matrix = [
        [' ',' ', 2 , 7 ,' ',' ', 1 , 5 , 6 ],
        [' ', 3 ,' ', 6 , 2 , 8 ,' ', 4 ,' '],
        [ 7 , 6 , 9 ,' ',' ',' ',' ', 3 ,' '],
        [ 9 ,' ', 7 ,' ', 4 , 5 , 3 ,' ',' '],
        [' ',' ',' ',' ', 8 ,' ', 7 , 2 ,' '],
        [ 6 , 2 ,' ', 3 ,' ',' ', 5 ,' ',' '],
        [' ', 5 ,' ', 1 ,' ', 3 ,' ',' ', 9 ],
        [' ', 7 ,' ',' ', 9 ,' ', 2 ,' ', 5 ],
        [ 4 ,' ', 1 , 5 , 7 ,' ',' ',' ',' ']
    ]
    
    for x in range(9):
        for y in range(9):
            if isinstance(matrix[x][y], int) == True:
                assert int(puzzle.squares[x][y]['value']) == matrix[x][y]
            else:
                assert puzzle.squares[x][y]['value'] == matrix[x][y]