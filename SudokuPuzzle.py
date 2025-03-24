class SudokuPuzzle:
    def __init__(self):
        self.squares = [ [{'value': "", 'possible_values': []} for x in range(9)] for y in range(9)]
        self.guessing_used = False
        self.analysis_helped = False

    # def is_valid(self):
    # Add a method to check if the puzzle status is valid

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

        return True