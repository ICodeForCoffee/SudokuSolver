from sudoku_solver import SudokuSolver
from sudoku_puzzle import SudokuPuzzle
import pytest

def test_basic_solving():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
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
            puzzle.squares[x][y]['initial_value'] = False

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
            puzzle.squares[x][y]['initial_value'] = False

def test_simple_solving():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
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
            puzzle.squares[x][y]['initial_value'] = False

    
    assert puzzle.is_solved() == False
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True
    assert puzzle.guessing_used == False

def test_complex_solving_one():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
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
            puzzle.squares[x][y]['initial_value'] = False

    
    assert puzzle.is_solved() == False
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True

def test_complex_solving_two():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
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
            puzzle.squares[x][y]['initial_value'] = False

    
    assert puzzle.is_solved() == False
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True

def test_locked_candidates_analysis_method():
    # TODO Need to verify if I'm keeping the method this code tests
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
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
            puzzle.squares[x][y]['initial_value'] = False

    assert puzzle.is_solved() == False
    
    # Check that analysis calculates the value at 7, 4
    instance.populate_possible_values(puzzle)
    assert puzzle.squares[7][4]['value'] == ' '
    assert len(puzzle.squares[7][4]['possible_values']) == 3
    change_made = instance.locked_candidates_analysis(puzzle, 7, 4)
    assert change_made == True
    
    instance.naked_single(puzzle)
    assert puzzle.squares[7][4]['value'] == 4
    
    puzzle = instance.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True

def test_load_function():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
    puzzle = instance.load_puzzle("Puzzles\\sudoku-puzzle1.txt")
    
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
                

def test_load_function_initial_value():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
    puzzle = instance.load_puzzle("Puzzles\\sudoku-puzzle1.txt")
    
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
    
    assert puzzle.squares[0][0]['initial_value'] == False
    assert puzzle.squares[0][1]['initial_value'] == False
    assert puzzle.squares[0][2]['initial_value'] == True
    assert puzzle.squares[1][1]['initial_value'] == True
    assert puzzle.squares[0][0]['value'] == ' '
    assert int(puzzle.squares[1][1]['value']) == 3
    
def test_guessing_function():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
    # This is the same Matrix from sudoku-puzzle1.txt
    matrix = [
        [' ',' ',' ', 7 , 8 ,' ', 6 , 3 , 9 ],
        [' ',' ',' ', 9 ,' ',' ', 7 , 5 , 2 ],
        [ 7 ,' ',' ', 5 ,' ',' ', 8 , 1 , 4 ],
        [' ', 7 ,' ',' ',' ', 5 , 1 ,' ',' '],
        [' ', 8 ,' ', 6 , 9 ,' ',' ', 4 , 7 ],
        [' ', 3 ,' ',' ', 2 , 7 ,' ',' ',' '],
        [' ',' ', 7 ,' ',' ', 6 ,' ',' ', 1 ],
        [' ',' ', 1 ,' ', 5 ,' ',' ', 7 ,' '],
        [' ', 5 ,' ',' ', 7 ,' ', 4 ,' ', 6 ]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]
            puzzle.squares[x][y]['initial_value'] = False

    assert puzzle.is_solved() == False
    
    # Have the puzzle guess a value and make sure it solves the puzzle.
    puzzle.guessing_used = False
    instance.populate_possible_values(puzzle)
    puzzle = instance.guess_a_value(puzzle)
    assert puzzle.is_solved() == True
    
    
def test_populate_possible_values():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=False)
    
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
            puzzle.squares[x][y]['initial_value'] = False
    
    instance.populate_possible_values(puzzle)
    possible_value_array = puzzle.squares[3][4]['possible_values']
    expected_value_array = [6]
    
    assert possible_value_array == expected_value_array
    
    puzzle2 = SudokuPuzzle()
    
    # This is the same Matrix from sudoku-puzzle1.txt
    matrix = [
        [' ',' ',' ', 7 , 8 ,' ', 6 , 3 , 9 ],
        [' ',' ',' ', 9 ,' ',' ', 7 , 5 , 2 ],
        [ 7 ,' ',' ', 5 ,' ',' ', 8 , 1 , 4 ],
        [' ', 7 ,' ',' ',' ', 5 , 1 ,' ',' '],
        [' ', 8 ,' ', 6 , 9 ,' ',' ', 4 , 7 ],
        [' ', 3 ,' ',' ', 2 , 7 ,' ',' ',' '],
        [' ',' ', 7 ,' ',' ', 6 ,' ',' ', 1 ],
        [' ',' ', 1 ,' ', 5 ,' ',' ', 7 ,' '],
        [' ', 5 ,' ',' ', 7 ,' ', 4 ,' ', 6 ]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle2.squares[x][y]['value'] = matrix[x][y]
            puzzle.squares[x][y]['initial_value'] = False

    instance.populate_possible_values(puzzle2)
    possible_value_array = puzzle2.squares[3][4]['possible_values']
    expected_value_array = [3, 4]
    
    assert possible_value_array == expected_value_array
    
    possible_value_array = puzzle2.squares[0][0]['possible_values']
    expected_value_array = [1, 2, 4, 5]
    
    assert possible_value_array == expected_value_array
    
def test_logging_of_steps():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=True)
    
    # The missing value here is 6.
    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, ' ', 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2,' ', 4],
        [2,' ', 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]
            puzzle.squares[x][y]['initial_value'] = False

    assert puzzle.is_solved() == False
    puzzle = instance.start_solving(puzzle)
    assert puzzle.is_solved() == True
    assert len(instance.steps) == 4
    
    
def test_is_solvable():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=True)

    matrix = [
        [ 6 , 1 , 2 , 7 , 8 , 4 , 5 , 3 , 9 ],
        [ 5 , 4 , 8 , 9 ,' ', 3 , 7 ,' ', 2 ],
        [ 7 , 9 , 3 , 5 ,' ', 2 , 8 ,' ', 4 ],
        [ 9 , 7 , 6 , 4 , 3 , 5 , 1 , 2 , 8 ],
        [ 2 , 8 , 5 , 6 , 9 , 1 , 3 , 4 , 7 ],
        [ 1 , 3 , 4 , 8 , 2 , 7 , 6 ,' ', 5 ],
        [ 8 , 2 , 7 , 3 , 4 , 6 , 9 , 5 , 1 ],
        [' ',' ', 1 , 2 , 5 ,' ',' ', 7 , 3 ],
        [' ', 5 ,' ', 1 , 7 ,' ', 4 ,' ', 6 ]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]
            puzzle.squares[x][y]['initial_value'] = False
    
    instance.populate_possible_values(puzzle)
    
def test_get_possible_pairs():
    instance = SudokuSolver(log_gui_display=True)
    
    possible_pairs = [3, 5, 7]
    results = instance.get_possible_pairs(possible_pairs)
    
    assert [3, 5] in results
    assert [3, 7] in results
    assert [5, 7] in results
    
    possible_pairs = [1, 3, 4, 5, 7, 9]
    results = instance.get_possible_pairs(possible_pairs)
    
    assert [4, 9] in results
    assert [1, 7] in results
    assert [5, 7] in results
    
    possible_pairs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results = instance.get_possible_pairs(possible_pairs)
    
    assert len(results) == 36
    assert [1, 9] in results
    assert [4, 9] in results
    assert [1, 7] in results
    assert [5, 7] in results

def test_hidden_pairs_check():
    puzzle = SudokuPuzzle()
    instance = SudokuSolver(log_gui_display=True)

    matrix = [
        [' ', 4 , 9 , 1 , 3 , 2 ,' ',' ',' '],
        [' ', 8 , 1 , 4 , 7 , 9 ,' ',' ',' '],
        [ 3 , 2 , 7 , 6 , 8 , 5 , 9 , 1 , 4 ],
        [' ', 9 , 6 ,' ', 5 , 1 , 8 ,' ',' '],
        [' ', 7 , 5 ,' ', 2 , 8 ,' ',' ',' '],
        [' ', 3 , 8 ,' ', 4 , 6 ,' ',' ', 5 ],
        [ 8 , 5 , 3 , 2 , 6 , 7 ,' ',' ',' '],
        [ 7 , 1 , 2 , 8 , 9 , 4 , 5 , 6 , 3 ],
        [ 9 , 6 , 4 , 5 , 1 , 3 ,' ',' ',' ']
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]
            puzzle.squares[x][y]['initial_value'] = False
    
    instance.populate_possible_values(puzzle)
    
    possibilities = [1, 9]
    current_list_in_square = [1, 6, 9]
    
    assert puzzle.squares[4][8]['possible_values'] == current_list_in_square
    assert puzzle.squares[6][8]['possible_values'] == possibilities
    
    result = instance.hidden_pairs_check(puzzle, 4, 8, possibilities)
    
    assert result == True
    assert puzzle.squares[4][8]['possible_values'] == possibilities
    assert puzzle.squares[6][8]['possible_values'] == possibilities