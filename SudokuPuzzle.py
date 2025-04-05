# Represents a Sudoku puzzle
class SudokuPuzzle:
    def __init__(self):
        self.squares = [ [{'value': "", 'possible_values': [], 'initial_value:': "", 'is_guess': ""} for x in range(9)] for y in range(9)]
        self.guessing_used = False
        self.analysis_helped = False
        self.last_square_x = ''
        self.last_square_y = ''

    # Confirms the puzzle is solved and the puzzle is valid
    def is_solved(self):
        value_list = list(range(1, 10))

        for x in range(9):
            found_values = []
            for y in range(9):
                if self.squares[x][y]['value'] == " ":
                    return False

                found_values.append(int(self.squares[x][y]['value']))
            found_values.sort()

            if value_list != found_values:
                return False

        for y in range(9):
            found_values = []
            for x in range(9):

                found_values.append(int(self.squares[x][y]['value']))
            found_values.sort()

            if value_list != found_values:
                return False

        for box_x in range(3):
            for box_y in range(3):
                found_values = []
                
                square_array = [0, 1, 2]
                
                for x in square_array:
                    for y in square_array:
                        if self.squares[x + (3* box_x)][y + (3 * box_y)]['value'] == " ":
                            return False

                        found_values.append(int(self.squares[x + (3 * box_x)][y + (3 * box_y)]['value']))
                
                found_values.sort()
                if value_list != found_values:
                    return False

        return True
    
    # Sets a square and logs that a square was solved
    # The last square values are used in the GUI display
    def set_square(self, x, y, value):
        self.squares[x][y]['value'] = value
        self.last_square_x = x
        self.last_square_y = y
        self.squares[x][y]['possible_values'] = []