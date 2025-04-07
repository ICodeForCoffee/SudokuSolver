# Sudoku Solver

Solves Suddoku. This project has a main() file, two class files, and multiple test files you can run through the application.

## Usage

To call the application use `python sudoku.py -file PUZZLE_TO_SOLVE`.

Puzzles for the application are [located in a folder](https://github.com/ICodeForCoffee/SudokuSolver/tree/main/Puzzles).

The code also supports a number of flags. By default the program runs in the console, but it supports a graphical mode using NiceGUI.

- `-file`/`-f` - Specifies the file to display
- `-d` - Turn on the visualizer using a web browser.
- `-n` - Turn on the visualizer in native window mode. The application still runs a web server to do this.
- `-np` - Turns off possible values in the visualizer. Has no affect in console mode.
- `-v` - Displays lots of debugging messages to the console. Will not do anything if you turned off debugging in python with `-O`.

## File Breakdown

- main.py - main() - [View file.](https://github.com/ICodeForCoffee/SudokuSolver/blob/main/main.py)
- sudoku_puzzle.py - Class that represents a Sudoku puzzle - [View file.](https://github.com/ICodeForCoffee/SudokuSolver/blob/main/sudoku_puzzle.py)
- sudoku_solver.py - Class with logic for solving a Sudoku puzzle - [View file.](https://github.com/ICodeForCoffee/SudokuSolver/blob/main/sudoku_solver.py)
- sudoku_visualizer.py - GUI launcher and logic - [View file.](https://github.com/ICodeForCoffee/SudokuSolver/blob/main/sudoku_visualizer.py)

This application includes unit tests in

- sudoku_puzzle_test.py - [View file.](https://github.com/ICodeForCoffee/SudokuSolver/blob/main/Tests/sudoku_puzzle_test.py)
- sudoku_solver_test.py - [View file.](https://github.com/ICodeForCoffee/SudokuSolver/blob/main/Tests/sudoku_solver_test.py)
- sudoku_visualizer_test.py - [View file.](https://github.com/ICodeForCoffee/SudokuSolver/blob/main/Tests/sudoku_visualizer_test.py)

## GUI Example

<img width="556" alt="SudokuAppExample" src="https://github.com/user-attachments/assets/5bea2b61-10e9-45d2-9c1a-a983abda20d3" />
