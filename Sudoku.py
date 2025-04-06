from SudokuSolver import SudokuSolver
from SudokuVisualizer import SudokuVisualizer
import argparse
import time
import copy

display = False
hide = False
verbose = False

def main():
    parser = argparse.ArgumentParser(prog="Sudoku Solver", description="Sudoku Solver")
    parser.add_argument("-file", help="Sudoku problem to solve", required=True, type=str)
    parser.add_argument("-d", "--display", help="Turn on the visualizer", action="store_true", required=False)
    parser.add_argument("-np", help="Turns off possible values in the visualizer", action="store_true", required=False)
    parser.add_argument("-v", "--verbose", help="Display all debug code", action="store_true", required=False)
    args = parser.parse_args()
    
    #Store the flags.
    display_flag = False
    hide_possible_values_flag = False
    verbose_flag = False
    if args.display == True:
        display_flag = True
    if args.np == True:
        hide_possible_values_flag = True
    if args.verbose == True:
        verbose_flag = True

    instance = SudokuSolver(log_gui_display=True)
    puzzle = instance.load_puzzle(args.file)

    if display_flag == True:
        run_display_mode(puzzle, hide_possible_values_flag)
    else:
        run_console_mode(puzzle, verbose_flag)

def run_console_mode(puzzle, verbose_flag):
    instance = SudokuSolver(log_gui_display=False)
        
    print("Initial puzzle\n")
    instance.display_puzzle_to_console(puzzle)
    
    start_time = time.time()
    puzzle = instance.start_solving(puzzle)
    end_time = time.time()
    
    print("After attempting to solve\n")
    instance.display_puzzle_to_console(puzzle)
    
    print(f"This puzzle is {"solved" if puzzle.is_solved() == True else "unsolved"}")
    if __debug__:
        if puzzle.guessing_used == True or puzzle.analysis_helped == True:
            print()
        if puzzle.guessing_used == True:
            print(f"Guessing was used to calculate this result")
        if puzzle.analysis_helped == True:
            print("The analysis method helped")
    time_elapsed = end_time - start_time
    print()
    print(f"The solving method took {time_elapsed:.5f} seconds.")
    print(f"The solution took {len(instance.steps)} steps.")
    print()

def run_display_mode(puzzle, hide_possible_values_flag):
    instance = SudokuSolver(log_gui_display=True)
    visualizer = SudokuVisualizer()
    print("Run the display")
    instance.populate_possible_values(puzzle)
    puzzle = instance.start_solving(puzzle)
    visualizer.render_gui(instance.steps)

main()