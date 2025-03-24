from SudokuSolver import SudokuSolver
from SudokuVisualizer import SudokuVisualizer
import argparse
import time
import copy

def main():
    parser = argparse.ArgumentParser(prog="Sudoku Solver", description="Sudoku Solver")
    parser.add_argument("-file", help="Sudoku problem to solve", required=True, type=str)
    parser.add_argument("-d", "--display", help="Turn on the visualizer", action="store_true", required=False)
    #parser.add_argument("-v", "--verbose", help="Display all debug code", action="store_true", required=False)
    args = parser.parse_args()
    
    instance = SudokuSolver()
    visualizer = SudokuVisualizer()
    puzzle = instance.load_puzzle(args.file)
    
    print("Initial puzzle\n")
    if args.display or 1 == 1:
        print("Run the display")
        instance.populate_possible_values(puzzle)
        #trying to foce a copy for display first.
        puzzle2 = copy.deepcopy(puzzle)
        visualizer.display_puzzle_to_website(puzzle2)
    
    #Code below will have to change to work with the display
    instance.display_puzzle_to_console(puzzle)
    
    start_time = time.time()
    puzzle = instance.solve_puzzle(puzzle)
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
    print()

main()