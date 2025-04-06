class SudokuPuzzle:
    ###Represents a Sudoku puzzle.###
    def __init__(self):
        self.squares = [ [{'value': "", 'possible_values': [], 'initial_value:': "", 'is_guess': ""} for x in range(9)] for y in range(9)]
        self.guessing_used = False
        self.analysis_helped = False
        self.last_square_x = ''
        self.last_square_y = ''

    
    def is_solved(self):
        ###Confirms the puzzle is solved and the puzzle is valid.###
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
    
    def is_solvable(self):
        ###Check to see if every unsolved square has possible values.###
        
        # Is solveable returns true if the puzzle is solved right now
        # Possible values must be set in order to use this function
        unsolved = False
        
        # Do all squares have a possible value if not filled in.
        for x in range(9):
            for y in range(9):
                if self.squares[x][y]['value'] == " " and len(self.squares[x][y]['possible_values']) == 0:
                    return False
                elif self.squares[x][y]['value'] == " ":
                    unsolved = True
        
        return True
    
    def set_square(self, x, y, value):
        ###Sets the value of a square.###
        
        # The last square values are used in the GUI display
        self.squares[x][y]['value'] = value
        self.last_square_x = x
        self.last_square_y = y
        self.squares[x][y]['possible_values'] = []